from typing import TYPE_CHECKING, Annotated

from fastapi import BackgroundTasks, Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from tmpauth.db.models import AccessToken, User
from tmpauth.services.authentication.user_manager import UserManager

from common.sqlalchemy.dependencies import get_db_session

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_tokens_db(
    session: Annotated[
        "AsyncSession",
        Depends(get_db_session),
    ],
):
    """
    Получение доступа к БД с токенами доступа.

    :param session: Сессия БД
    :Yields: Токен доступа
    """
    yield AccessToken.get_db_token(session=session)


async def get_users_db(
    session: Annotated[
        "AsyncSession",
        Depends(get_db_session),
    ],
):
    """
    Получение доступа к БД с пользователями.

    :param session: Сессия БД
    :Yields: Пользователь
    """
    yield User.get_db_user(session=session)


async def get_user_manager(
    users_db: Annotated[
        "SQLAlchemyUserDatabase",
        Depends(get_users_db),
    ],
    background_tasks: BackgroundTasks,
):
    """
    Получение менеджера пользователей.

    :param users_db: БД с пользователями
    :param background_tasks: Задачи в фоновом режиме
    :Yields: Менеджер пользователей
    """
    yield UserManager(
        users_db,
        background_tasks=background_tasks,
    )
