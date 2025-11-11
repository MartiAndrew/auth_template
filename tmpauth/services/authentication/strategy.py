from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy
from tmpauth.services.authentication.dependencies import get_access_tokens_db

from configuration.settings import settings

if TYPE_CHECKING:
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase
    from tmpauth.db.models import AccessToken


def get_database_strategy(
    access_tokens_db: Annotated[
        "AccessTokenDatabase[AccessToken]",
        Depends(get_access_tokens_db),
    ],
) -> DatabaseStrategy:
    """
    Получить стратегию аутентификации через БД.

    :param access_tokens_db: БД токенов доступа.
    :return: Стратегия аутентификации через БД.
    """
    return DatabaseStrategy(
        database=access_tokens_db,
        lifetime_seconds=settings.auth.lifetime_seconds,
    )
