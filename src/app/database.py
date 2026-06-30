from collections.abc import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings

engine = create_engine(
    settings.get_database_url(),
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_db_connection() -> dict:
    with engine.connect() as conn:
        return {
            "database": conn.execute(text("SELECT current_database()")).scalar_one(),
            "user": conn.execute(text("SELECT current_user")).scalar_one(),
            "version": conn.execute(text("SELECT version()")).scalar_one(),
        }
