from typing import (
    TYPE_CHECKING,
    Annotated,
)

from fastapi import Depends

from common.sqlalchemy.dependencies import get_db_session
from tmpauth.db.models import AccessToken, User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_tokens_db(
    session: Annotated[
        "AsyncSession",
        Depends(get_db_session),
    ],
):
    yield AccessToken.get_db_token(session=session)


async def get_users_db(
    session: Annotated[
        "AsyncSession",
        Depends(get_db_session),
    ],
):
    yield User.get_db_user(session=session)
