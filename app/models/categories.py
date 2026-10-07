# models/categories.py
from sqlalchemy.orm import Mapped

from app.models.base import Base


class CategoriesModel(Base):
    __tablename__ = "categories"

    name: Mapped[str]