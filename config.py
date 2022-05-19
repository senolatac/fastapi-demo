import os
from typing import Union

from pydantic import BaseSettings


class Base(BaseSettings):
    admin_key_token: str = "admin"
    secure_key_token: str = "user1,user2"

    class Config:
        env_file = ".env"


class Default(Base):
    env = "default"

    class Config:
        env_file = '.env'


class Test(Base):
    env = "test"

    class Config:
        env_file = 'test.env'


config = dict(
    default=Default,
    test=Test
)

settings: Union[Default, Test] = config[os.environ.get('ENV', 'default').lower()]()
