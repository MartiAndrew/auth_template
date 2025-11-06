from sqlalchemy.orm import Mapped, mapped_column
from tmpauth.db.models import Base


class User(Base):
    """Модель пользователя."""

    user: Mapped[str] = mapped_column(unique=True)
