# api/routers/task.py
from fastapi import APIRouter, status, Depends, HTTPException

from app.api.dependencies import db_dependence
from app.schemas.tasks import STaskRead, STaskAdd, STaskUpdate
from app.services.task_service import TaskService

router_tasks = APIRouter(prefix="/tasks", tags=["tasks"])

@router_tasks.get("")
def get_tasks(task_service: TaskService = Depends(db_dependence)) -> list[STaskRead]:
    return task_service.list_tasks()

@router_tasks.post("", status_code=status.HTTP_201_CREATED)
def add_task(task: STaskAdd, task_service: TaskService = Depends(db_dependence)) -> STaskRead:
    return task_service.create_task(task)

@router_tasks.patch("/{task_id}")
def update_task(task: STaskUpdate, task_id: str, task_service: TaskService = Depends(db_dependence)) -> STaskRead:
    updated_task = task_service.update_task(task, task_id)

    if updated_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    return updated_task

@router_tasks.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str, task_service: TaskService = Depends(db_dependence)) -> None:
    task_service.remove_task(task_id)
