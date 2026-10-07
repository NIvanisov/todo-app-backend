# api/routers/dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session

from app.databases.database import get_db
from app.services.category_service import CategoryService
from app.services.task_service import TaskService


def db_dependence(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)

def get_category_service(db: Session = Depends(get_db)) -> CategoryService:
    return CategoryService(db)