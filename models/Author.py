from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func


def create_model_author(Base):
    class Author(Base):
        __tablename__ = "authors"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        age = Column(Integer)
        time_created = Column(DateTime(timezone=True),
                              server_default=func.now())
    return Author
