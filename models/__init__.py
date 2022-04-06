from sqlalchemy.ext.declarative import declarative_base
from models.Author import create_model_author
from models.Book import create_model_book

Base = declarative_base()

Book = create_model_book(Base)
Author = create_model_author(Base)
