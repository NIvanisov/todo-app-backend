# repositories/repository.py
from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from typing import Sequence

from app.models.tasks import TasksModel
from app.schemas.tasks import STaskAdd, STaskUpdate


class TaskRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def select_tasks(self) -> Sequence[TasksModel]:
        query = select(TasksModel)
        tasks = self.db.execute(query)
        return tasks.scalars().all()

    def insert_task(self, task: STaskAdd) -> TasksModel:
        new_task = TasksModel(**task.model_dump())
        self.db.add(new_task)
        return new_task

    def update_task(self, task: STaskUpdate, task_to_upd: TasksModel) -> None:
        for k, v in task.model_dump(exclude_unset=True).items():
            setattr(task_to_upd, k, v)

    def select_task(self, task_id: str) -> TasksModel | None:
        return self.db.get(TasksModel, task_id)

    def delete_task(self, task_id: str) -> None:
        stmt = delete(TasksModel).where(TasksModel.id == task_id)
        self.db.execute(stmt)