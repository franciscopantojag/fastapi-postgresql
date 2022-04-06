from pydantic import BaseModel


class Author(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True
