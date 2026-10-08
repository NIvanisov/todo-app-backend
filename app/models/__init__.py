from app.models.base import Base
# Импорт моделей, чтобы зарегистрировать их в Base.metadata
from app.models.tasks import TasksModel
from app.models.categories import CategoriesModel

__all__ = ["Base", "TasksModel", "CategoriesModel"]