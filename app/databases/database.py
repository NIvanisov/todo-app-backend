# databases/database.py
from contextlib import asynccontextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

from app.models.tasks import Base
from app.core.config import get_settings

settings = get_settings()
engine = create_engine(settings.DATABASE_URL)

SessionFabric = sessionmaker(bind=engine)

@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

def get_db():
    db = SessionFabric()
    try:
        yield db
    finally:
        db.close()