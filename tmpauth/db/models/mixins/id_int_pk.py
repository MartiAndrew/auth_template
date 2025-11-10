from sqlalchemy.orm import Mapped, mapped_column


class IdIntPkMixin:
    """Миксин для моделей с целочисленным первичным ключом."""

    id: Mapped[int] = mapped_column(primary_key=True)