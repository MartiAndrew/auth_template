"""Модели БД."""

from tmpauth.db.models.access_token import AccessToken
from tmpauth.db.models.user import User

__all__ = [
    "User",
    "AccessToken",
]
