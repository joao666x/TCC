import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USERNAME = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASS')
HOST = os.environ.get('DB_HOST')
PORT = os.environ.get('DB_PORT')
DB_DB = os.environ.get('DB_DB')

def get_db_engine():
    return create_engine(
        f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_DB}",
        echo=True,
        future=True
    )


def get_session() -> sessionmaker:
    engine = create_engine(
        f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_DB}",
        echo=True,
        future=True
    )
    return sessionmaker(engine)
