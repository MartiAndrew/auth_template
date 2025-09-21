"""Модели БД."""
from db.models.base_model import Base
from db.models.user import User

__all__ = [
    "Base",
    "User",
]
