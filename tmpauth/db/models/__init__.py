"""Модели БД."""
from tmpauth.db.models.base_model import Base
from tmpauth.db.models.user import User
from tmpauth.db.models.access_token import AccessToken

__all__ = [
    "Base",
    "User",
    "AccessToken"
]
