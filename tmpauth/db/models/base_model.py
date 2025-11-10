from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr

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
