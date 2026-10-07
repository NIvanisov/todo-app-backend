# services/task_service.py
from sqlalchemy.orm import Session

from app.cache.redis_tasks import RedisCacheTasks
from app.repositories.task_repository import TaskRepository
from app.models.tasks import TasksModel
from app.schemas.tasks import STaskRead, STaskAdd, STaskUpdate
from app.core.config import get_settings

settings = get_settings()

class TaskService:
    """
    Класс для ключевых операций с задачами

    Выполнение основной бизнес логики, валидации
    """
    def __init__(self, db: Session) -> None:
        self.db = db
        self.cache = RedisCacheTasks(settings.redis_url, settings.cache_ttl_seconds)
        self.task_repository = TaskRepository(db)

    def list_tasks(self) -> list[STaskRead]:
        tasks = self.cache.get(settings.cache_tasks_key)
        if tasks is not None:
            return tasks

        tasks = self.task_repository.select_tasks()

        tasks = [STaskRead.model_validate(task) for task in tasks]
        self.cache.set(settings.cache_tasks_key, [task.model_dump() for task in tasks])
        return tasks

    def create_task(self, task: STaskAdd) -> TasksModel:
        self.cache.delete(settings.cache_tasks_key)

        new_task = self.task_repository.insert_task(task)
        self.db.commit()
        self.db.refresh(new_task)
        return new_task

    def update_task(self, task: STaskUpdate, task_id: str) -> TasksModel | None:
        self.cache.delete(settings.cache_tasks_key)

        task_to_update = self.task_repository.select_task(task_id)
        if task_to_update is None:
            return None
        self.task_repository.update_task(task, task_to_update)
        self.db.commit()
        self.db.refresh(task_to_update)
        return task_to_update

    def remove_task(self, task_id) -> None:
        self.cache.delete(settings.cache_tasks_key)

        self.task_repository.delete_task(task_id)
        self.db.commit()