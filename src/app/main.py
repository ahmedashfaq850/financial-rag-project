from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.config import settings
from app.database import check_db_connection, get_db

app = FastAPI(title="RAG Project", debug=settings.debug)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "environment": settings.environment}


@app.get("/health/db")
def health_db(db: Session = Depends(get_db)) -> dict:
    del db  # connection verified by dependency
    return {"status": "ok", **check_db_connection()}
