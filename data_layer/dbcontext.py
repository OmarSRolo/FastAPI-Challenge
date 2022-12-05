from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AlchemyDBContext:
    def __init__(self, url_connection: str):
        self.engine = create_engine(url_connection)

    def create_models(self) -> None:
        Base.metadata.create_all(bind=self.engine)
