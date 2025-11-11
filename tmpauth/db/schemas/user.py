from datetime import datetime

from fastapi_users import schemas
from pydantic import BaseModel, Field

from configuration.types import UserIdType


class UserRead(schemas.BaseUser[UserIdType]):
    """Схема для чтения пользователя (ответ от API)."""

    nickname: str | None = None
    avatar: str | None = None
    about: str | None = None
    created_at: datetime


class UserCreate(schemas.BaseUserCreate):
    """Схема для создания пользователя (регистрация)."""

    nickname: str | None = Field(None, max_length=25)
    avatar: str | None = Field(None, max_length=250)
    about: str | None = Field(None, max_length=150)


class UserUpdate(schemas.BaseUserUpdate):
    """Схема для обновления профиля пользователя."""

    nickname: str | None = Field(None, max_length=25)
    avatar: str | None = Field(None, max_length=250)
    about: str | None = Field(None, max_length=150)


class UserRegisteredNotification(BaseModel):
    """Схема для уведомления о регистрации пользователя."""

    user: UserRead
    ts: int
