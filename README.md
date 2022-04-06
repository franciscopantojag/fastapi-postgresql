# FastAPI postgresql Example
Example of a REST API using the FastAPI web framework from Python, and a PostgreSQL db

## Requirements
- Docker

## Installation/Run Migrations

1. `docker-compose build`
2. `docker-compose up`
3. On a different terminal run:
    - `docker-compose run app alembic revision --autogenerate -m "New Migration"`
    - `docker-compose run app alembic upgrade head`
5. Go to `http://localhost:8000/docs`

