from pydantic import BaseModel


class Book(BaseModel):
    title: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True
