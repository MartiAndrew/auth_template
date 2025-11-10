from pathlib import Path

from loguru import logger
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from common.sqlalchemy.tests.alembic_helper import run_alembic_upgrade

from configuration import clients
from configuration.constants import SERVICE_NAME_LOWER, SERVICE_PATH
from configuration.settings import settings

SQL_CLEAR_TEST_DB_PATH = Path(
    f"{SERVICE_PATH}/db/service_db/sql/clear_testdb.sql",
)


async def drop_db() -> None:
    """Дропнуть тестовую БД после всех тестов."""
    logger.info("drop test db")

    admin_url = settings.sqlalchemy_db.url.set(database="postgres")
    admin_engine = create_async_engine(admin_url, isolation_level="AUTOCOMMIT")

    async with admin_engine.begin() as conn:
        await conn.execute(
            text(
                """
                SELECT pg_terminate_backend(pg_stat_activity.pid)
                FROM pg_stat_activity
                WHERE pg_stat_activity.datname = :dbname
                AND pid <> pg_backend_pid();
                """
            ),
            {"dbname": settings.sqlalchemy_db.base_name},
        )

        drop_db_query = f"DROP DATABASE {settings.sqlalchemy_db.base_name};"
        await conn.execute(text(drop_db_query))

    await admin_engine.dispose()


async def create_db() -> None:
    """Создать тестовую БД."""
    logger.info("create test db")

    admin_url = settings.sqlalchemy_db.url.set(database="postgres")
    admin_engine = create_async_engine(admin_url, isolation_level="AUTOCOMMIT")

    async with admin_engine.begin() as conn_check:
        result = await conn_check.execute(
            text("SELECT 1 FROM pg_database WHERE datname=:dbname"),
            {"dbname": settings.sqlalchemy_db.base_name},
        )
        exists = result.scalar() is not None

    if exists:
        await drop_db()

    async with admin_engine.begin() as conn_create:
        create_db_query = f"CREATE DATABASE {settings.sqlalchemy_db.base_name};"
        await conn_create.execute(text(create_db_query))

    await admin_engine.dispose()


def get_service_db_lifetime(sqlalchemy_engine: AsyncEngine):
    """
    Получить функции для инициализации мока.

    :return: функции старта и завершения.
    """

    async def startup():  # noqa: WPS430
        return sqlalchemy_engine

    async def shutdown(engine: AsyncEngine):  # noqa: WPS430
        async with engine.begin() as conn:
            await conn.execute(text(SQL_CLEAR_TEST_DB_PATH.read_text()))

    return startup, shutdown


async def sqlalchemy_engine_init(worker_id: str) -> AsyncEngine:
    """
    Мок SQLAlchemy engine.

    :return: mocked AsyncEngine
    """
    db_base = f"{SERVICE_NAME_LOWER}_sqlalchemy_db_test_{worker_id}"
    settings.sqlalchemy_db.base_name = db_base
    await create_db()

    engine = create_async_engine(
        url=settings.sqlalchemy_db.url,
        echo=settings.sqlalchemy_db.echo,
        pool_size=settings.sqlalchemy_db.pool_size,
        max_overflow=settings.sqlalchemy_db.max_overflow,
    )
    db_url = settings.sqlalchemy_db.url.render_as_string(hide_password=False)

    # миграции
    await run_alembic_upgrade(db_url)

    service_db_lifetime = get_service_db_lifetime(engine)
    clients.CLIENTS_LIFETIME["sqlalchemy_engine"] = service_db_lifetime

    return engine


async def sqlalchemy_engine_close(engine: AsyncEngine) -> None:
    """Закрыть SQLAlchemy engine и дропнуть тестовую базу."""
    await engine.dispose()
    await drop_db()
