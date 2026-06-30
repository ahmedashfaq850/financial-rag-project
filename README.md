<<<<<<< HEAD
# Financial Custom Rag System

## System Architecture Diagram

<img width="2720" height="2480" alt="Image" src="https://github.com/user-attachments/assets/725eddc2-3419-4f6e-8bd5-7e4056607c94" />

## Data Ingestion Pipeline

<img width="2720" height="2136" alt="Image" src="https://github.com/user-attachments/assets/e62f859b-6fe8-4669-893d-6dbdc4de4d40" />

## Data Retrieval Pipeline

<img width="2720" height="2120" alt="Image" src="https://github.com/user-attachments/assets/974c09c7-ba3b-469b-bbaf-5e3a5e17ff10" />

## Backend Architecture 

<img width="2720" height="2240" alt="Image" src="https://github.com/user-attachments/assets/352f112e-259e-4fe4-8c60-2f7913afe5eb" />
=======
# RAG Project

Minimal FastAPI + PostgreSQL boilerplate.

## Setup

```bash
cp .env.example .env   # add your DATABASE_URL
uv sync
```

## Run

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints

| Route | Description |
|---|---|
| `GET /health` | App health check |
| `GET /health/db` | PostgreSQL connection check |
| `GET /docs` | Swagger UI |

## Project structure

```
src/app/
├── main.py       # FastAPI app + routes
├── config.py     # Settings from .env
└── database.py   # SQLAlchemy engine + get_db()
```

## Database URL

Local development:

```
DATABASE_URL=postgresql://postgres:password@localhost:5433/mydatabase
```

Docker Compose (production):

```
DATABASE_URL=postgresql://postgres:password@postgres:5432/mydatabase
```

Never hardcode credentials in Python files. Keep them in `.env` only.
>>>>>>> d6705f1 (added new code)
