import os
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn
from routers import author, book
from fastapi_sqlalchemy import DBSessionMiddleware

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DB_URL"])


@app.get("/")
def index():
    return {"Hello": "World"}


app.include_router(author.router)
app.include_router(book.router)


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)
