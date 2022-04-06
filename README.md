# FastAPI postgresql Example
Example of a REST API built with the FastAPI web framework from Python, and a PostgreSQL db

## Requirements
- Docker

## Installation/Run

1. Create a .env file using the .env.example as a template
2. `docker-compose build`
3. `docker-compose up`
4. On a different terminal run:
    - `docker-compose run app alembic revision --autogenerate -m "New Migration"`
    - `docker-compose run app alembic upgrade head`
5. Go to `http://localhost:8000/docs`

