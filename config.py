from pydantic import BaseSettings


class Settings(BaseSettings):
    secure_key_token: str = "user1,user2"
    admin_key_token: str = "admin"

    class Config:
        env_file = ".env"


settings = Settings()
