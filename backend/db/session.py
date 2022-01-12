from typing import Generator
from sqlalchemy import create_engine, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

SQL_ALCHEMY_DATABASE_URL = "sqlite:///./mydatabase.db"
engine = create_engine(
    SQL_ALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    except:
        db = SessionLocal()
        db.close()
