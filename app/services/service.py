# services/service
from sqlalchemy.orm import Session
from typing import Sequence

from app.repositories.repository import TaskRepository
from app.models.tasks import TasksModel
from app.schemas.tasks import STaskAdd, STaskUpdate


class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.task_repository = TaskRepository(db)

    def list_tasks(self) -> Sequence[TasksModel]:
        return self.task_repository.select_tasks()

    def create_task(self, task: STaskAdd) -> TasksModel:
        new_task = self.task_repository.insert_task(task)
        self.db.commit()
        self.db.refresh(new_task)
        return new_task

    def update_task(self, task: STaskUpdate, task_id: str) -> TasksModel | None:
        task_to_update = self.task_repository.select_task(task_id)
        if task_to_update is None:
            return None
        self.task_repository.update_task(task, task_to_update)
        self.db.commit()
        self.db.refresh(task_to_update)
        return task_to_update

    def remove_task(self, task_id) -> None:
        self.task_repository.delete_task(task_id)
        self.db.commit()