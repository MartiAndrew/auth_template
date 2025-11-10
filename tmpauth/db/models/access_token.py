from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from tmpauth.db.models import Base

from configuration.types import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from common.auth.user import User


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[int]):
    user_id: Mapped[UserIdType] = mapped_column(
        Integer,
        ForeignKey("user.id", ondelete="cascade"),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        back_populates="access_tokens",
    )

    @classmethod
    def get_db_token(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)

    def __str__(self):
        return self.token
