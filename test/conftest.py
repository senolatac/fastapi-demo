import os
import sys
from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../../')
# this is to include backend dir in sys.path so that we can import from db,main.py

TEST_ENV_VARS = {
    'ENV': 'test'
}

os.environ["APP_ENV"] = "test"


def start_application():
    from app.main import get_application  # local import for testing purpose

    return get_application()


@pytest.fixture
def app() -> Generator[FastAPI, Any, None]:
    _app = start_application()
    yield _app


@pytest.fixture
def client(
        app: FastAPI
) -> Generator[TestClient, Any, None]:
    with TestClient(app) as client:
        yield client


@pytest.fixture
def tests_setup_and_teardown():
    # Will be executed before the first test
    old_environ = dict(os.environ)
    os.environ.update(TEST_ENV_VARS)

    yield
    # Will be executed after the last test
    os.environ.clear()
    os.environ.update(old_environ)
