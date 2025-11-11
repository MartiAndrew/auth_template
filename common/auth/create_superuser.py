import contextlib
from os import getenv

from fastapi import BackgroundTasks
from fastapi_users.exceptions import UserAlreadyExists
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker
from tmpauth.db.models import User
from tmpauth.db.schemas.user import UserCreate
from tmpauth.services.authentication.dependencies import get_user_manager, get_users_db
from tmpauth.services.authentication.user_manager import UserManager

from configuration.settings import settings

get_users_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


default_email = getenv("DEFAULT_EMAIL", settings.mail.admin_email)
default_password = getenv("DEFAULT_PASSWORD", "admin")
default_nickname = "admin"
default_is_active = True
default_is_superuser = True
default_is_verified = True


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    """Создание пользователя."""
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(
    engine: AsyncEngine,
    email: str = default_email,
    password: str = default_password,
    is_active: bool = default_is_active,
    is_superuser: bool = default_is_superuser,
    is_verified: bool = default_is_verified,
):
    """Создание суперпользователя."""
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )

    session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
    )
    background_tasks = BackgroundTasks()

    async with session_factory() as session:
        async with get_users_db_context(session) as users_db:
            async with get_user_manager_context(
                users_db, background_tasks
            ) as user_manager:
                try:
                    await create_user(
                        user_manager=user_manager,
                        user_create=user_create,
                    )
                except UserAlreadyExists as ex:
                    logger.warning(ex)
