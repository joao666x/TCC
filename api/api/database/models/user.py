from sqlalchemy import Column, String

from api.database.models.base import ApiBase

class User(ApiBase):

    name = Column(
        String
    )
    email = Column(
        String
    )
    password = Column(
        String
    )