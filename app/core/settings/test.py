import logging
from typing import Dict, Any

from pydantic import PostgresDsn, SecretStr

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "Test FastAPI example application"

    secret_key: SecretStr = SecretStr("test_secret")

    #database_url: PostgresDsn
    database_url = "sqlite:///:memory:"
    max_connection_count: int = 5
    min_connection_count: int = 5

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = "test.env"

    @property
    def connect_ags(self) -> Dict[str, Any]:
        return {
            "check_same_thread": False
        }
