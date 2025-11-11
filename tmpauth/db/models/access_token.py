from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from tmpauth.db.models.base_model import Base

from configuration.types import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[int]):
    """AccessToken модель."""

    user_id: Mapped[UserIdType] = mapped_column(
        Integer,
        ForeignKey("user.id", ondelete="cascade"),
        nullable=False,
    )

    @classmethod
    def get_db_token(cls, session: "AsyncSession") -> SQLAlchemyAccessTokenDatabase:
        """
        Получение токена из БД.

        :param session: Сессия БД.
        :return: Токен из БД.
        """
        return SQLAlchemyAccessTokenDatabase(session, cls)

    def __str__(self):
        return self.token
