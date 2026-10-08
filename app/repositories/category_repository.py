# repositories/category_repository.py
from sqlalchemy.orm import Session
from sqlalchemy import select, delete

from app.models import CategoriesModel
from app.schemas.categories import SCategoryAdd, SCategoryUpdate


class CategoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def select_categories(self) -> list[CategoriesModel]:
        query = select(CategoriesModel)
        result = self.db.execute(query)

        return result.scalars().all()

    def insert_category(self, category: SCategoryAdd) -> CategoriesModel:
        new_category = CategoriesModel(**category.model_dump())
        self.db.add(new_category)
        return new_category

    def update_category(self, category: CategoriesModel, data: SCategoryUpdate) -> CategoriesModel:
        for k, v in data.model_dump(exclude_unset=True).items():
            setattr(category, k, v)
        return category

    def select_category(self, category_id: str) -> CategoriesModel:
        return self.db.get(CategoriesModel, category_id)

    def delete_category(self, category_id: str) -> None:
        stmt = delete(CategoriesModel).where(CategoriesModel.id == category_id)
        self.db.execute(stmt)