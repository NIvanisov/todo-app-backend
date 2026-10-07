# services/category_service.py
from sqlalchemy.orm import Session

from app.repositories.category_repository import CategoryRepository
from app.schemas.categories import SCategoryAdd
from app.models.categories import CategoriesModel


class CategoryService:

    def __init__(self, db: Session) -> None:
        self.db = db
        self.repository = CategoryRepository(db)

    def get_categories(self) -> list[CategoriesModel]:
        return self.repository.select_categories()

    def add_category(self, category: SCategoryAdd) -> CategoriesModel:
        new_category = self.repository.insert_category(category)
        self.db.commit()
        self.db.refresh(new_category)
        return new_category

    def update_category(self, category_id: str, data: SCategoryAdd) -> CategoriesModel | None:

        category_to_upd = self.repository.select_category(category_id)

        if category_to_upd is None:
            return None

        updated_category = self.repository.update_category(category_to_upd, data)
        self.db.commit()
        return updated_category

    def delete_category(self, category_id: str) -> None:

        self.repository.delete_category(category_id)
        self.db.commit()