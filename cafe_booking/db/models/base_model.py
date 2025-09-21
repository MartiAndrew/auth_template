from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from common.utils.case_converter import camel_case_to_snake_case
from configuration.settings import settings


class Base(DeclarativeBase):
    """Класс базовой модели."""

    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.sqlalchemy_db.naming_convention,
    )

    @declared_attr.directive
    @classmethod
    def __tablename__(cls) -> str:
        return camel_case_to_snake_case(cls.__name__)

    id: Mapped[int] = mapped_column(primary_key=True)
