from datetime import datetime
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import DateTime, String, func

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import Mapped, mapped_column
from tmpauth.db.models.base_model import Base
from tmpauth.db.models.mixins.id_int_pk import IdIntPkMixin


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    """Модель пользователя."""

    nickname: Mapped[str | None] = mapped_column(
        String(length=25),
        unique=True,
        comment="Никнейм",
        nullable=True,
    )
    avatar: Mapped[str | None] = mapped_column(
        String(length=250),
        comment="Ссылка на аватар",
        nullable=True,
    )
    about: Mapped[str | None] = mapped_column(
        String(length=150),
        comment="О себе",
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        comment="Дата создания",
        server_default=func.now(),
    )

    @classmethod
    def get_db_user(cls, session: "AsyncSession") -> "SQLAlchemyUserDatabase":
        """
        Получить базу данных пользователей.

        :param session: Сессия базы данных.
        :return: База данных пользователей.
        """
        return SQLAlchemyUserDatabase(session, User)
