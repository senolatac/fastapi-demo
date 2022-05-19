import os
import sys
from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../../')
# this is to include backend dir in sys.path so that we can import from db,main.py

from src.route.api import router as api_router


def start_application():
    app = FastAPI()
    app.include_router(api_router)
    return app


@pytest.fixture(scope="module")
def app() -> Generator[FastAPI, Any, None]:
    _app = start_application()
    yield _app


@pytest.fixture(scope="module")
def client(
    app: FastAPI
) -> Generator[TestClient, Any, None]:
    with TestClient(app) as client:
        yield client
