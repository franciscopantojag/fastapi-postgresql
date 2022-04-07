from fastapi import APIRouter
from fastapi_sqlalchemy import db
from models import Author
from schemas.Author import Author as SchemaAuthor

router = APIRouter()


@router.get("/")
def get_authors():
    authors = db.session.query(Author).all()
    return authors


@router.post("/", response_model=SchemaAuthor)
def create_author(author: SchemaAuthor):
    db_author = Author(name=author.name, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author
