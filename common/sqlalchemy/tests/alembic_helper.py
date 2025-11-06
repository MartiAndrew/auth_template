import asyncio
from pathlib import Path

from alembic import command
from alembic.config import Config
from loguru import logger

from configuration.constants import SERVICE_PATH


async def run_alembic_upgrade(db_url: str):
    """Асинхронно применить все миграции через Alembic."""
    logger.info("Run alembic upgrade for test DB")

    alembic_cfg = Config(str(Path(__file__).parent.parent.parent.parent / "alembic.ini"))

    alembic_cfg.set_main_option("script_location", str(Path(SERVICE_PATH) / "db/alembic"))
    alembic_cfg.set_main_option("sqlalchemy.url", db_url)

    await asyncio.to_thread(command.upgrade, alembic_cfg, "head")