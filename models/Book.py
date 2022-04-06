from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


def create_model_book(Base):
    class Book(Base):
        __tablename__ = "books"
        id = Column(Integer, primary_key=True, index=True)
        title = Column(String)
        rating = Column(String)
        time_created = Column(DateTime(timezone=True),
                              server_default=func.now())
        time_updated = Column(DateTime(timezone=True), onupdate=func.now())
        author_id = Column(Integer, ForeignKey('authors.id'))

        author = relationship("Author")

    return Book
