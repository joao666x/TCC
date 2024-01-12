from datetime import datetime

import regex
from sqlalchemy import Column, Integer
from sqlalchemy.orm import as_declarative, declared_attr
from sqlalchemy.types import DateTime

@as_declarative()
class ApiBase(object):

    @declared_attr
    def __tablename__(self):
        """use the class name in CamelCase to generate
        the table's name in snake_case
        """
        return regex.sub(r'([a-z])([A-Z])', r'\1_\2', self.__name__).lower()

    id = Column(
        Integer,
        primary_key=True,
    )

    @declared_attr
    def created_at(cls):
        return Column(
            DateTime,
            default=datetime.utcnow
        )

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow
        )
