from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import get_app_settings

SETTINGS = get_app_settings()
engine = create_engine(SETTINGS.database_url, connect_args={"check_same_thread": False})

meta = MetaData()
conn = engine.connect()

SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)

Base = declarative_base()
