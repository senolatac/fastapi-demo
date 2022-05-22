from sqlalchemy import Column, BigInteger, String
from app.config.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True)
    name = Column(String(255))
    hashed_password = Column(String(255))
