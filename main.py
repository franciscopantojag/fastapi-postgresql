import os
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from schemas.Author import Author as SchemaAuthor
from schemas.Book import Book as SchemaBook
from models import Author as ModelAuthor, Book as ModelBook
from fastapi_sqlalchemy import DBSessionMiddleware, db

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DB_URL"])


@app.get("/")
def index():
    return {"Hello": "World"}


@app.post("/author")
def create_author(author: SchemaAuthor):
    db_author = ModelAuthor(name=author.name, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author


@app.post("/book")
def create_book(book: SchemaBook):
    db_book = ModelBook(title=book.title, rating=book.rating,
                        author_id=book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book


@app.get("/author")
def get_authors():
    authors = db.session.query(ModelAuthor).all()
    return authors


@app.get("/book")
def get_books():
    books = db.session.query(ModelBook).all()
    return books


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)
