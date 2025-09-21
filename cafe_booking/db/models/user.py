from sqlalchemy.orm import Mapped, mapped_column

from cafe_booking.db.models import Base


class User(Base):
    """Модель пользователя."""

    user: Mapped[str] = mapped_column(unique=True)
