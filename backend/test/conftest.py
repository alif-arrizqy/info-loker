import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from typing import Any
from typing import Generator

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.base import Base
from db.session import SQL_ALCHEMY_DATABASE_URL, get_db
from apis.base import api_router


def start_application():
    app = FastAPI()
    app.include_router(api_router)
    return app


SQL_ALCHEMY_DATABASE_URL = "sqlite:///./mydatabase.db"
engine = create_engine(
    SQL_ALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    Base.metadata.create_all(engine)  # create the tables
    _app = start_application()
    yield _app
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    conn = engine.connect()
    transaction = conn.begin()
    session = SessionTesting(bind=conn)
    yield session
    session.close()
    transaction.rollback()
    conn.close()


@pytest.fixture(scope="function")
def client(
    app: FastAPI, db_session: SessionTesting
) -> Generator[TestClient, Any, None]:
    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client
