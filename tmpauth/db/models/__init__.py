"""Модели БД."""
from tmpauth.db.models.base_model import Base
from tmpauth.db.models.user import User

__all__ = [
    "Base",
    "User",
]
