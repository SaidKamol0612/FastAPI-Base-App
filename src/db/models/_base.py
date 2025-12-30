from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy import MetaData

from core import settings
from core.utils import str_tools, pluralize


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return str_tools.to_snake_case(pluralize(cls.__name__))
