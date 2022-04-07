from fastapi import APIRouter
from fastapi_sqlalchemy import db
from models import Book
from schemas.Book import Book as SchemaBook

router = APIRouter()


@router.get("/")
def get_books():
    books = db.session.query(Book).all()
    return books


@router.post("/", response_model=SchemaBook)
def create_book(book: SchemaBook):
    db_book = Book(title=book.title, rating=book.rating,
                   author_id=book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book
