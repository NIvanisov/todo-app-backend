# api/routers/dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session

from app.databases.database import get_db
from app.services.service import TaskService


def db_dependence(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)