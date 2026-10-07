# api/routers/category.py
from fastapi import APIRouter, status, HTTPException, Depends

from app.api.dependencies import get_category_service
from app.schemas.categories import SCategoryRead, SCategoryAdd, SCategoryUpdate
from app.services.category_service import CategoryService

router_categories = APIRouter(prefix="/categories", tags=["categories"])

@router_categories.get("")
def get_categories(category_service: CategoryService = Depends(get_category_service)) -> list[SCategoryRead]:
    return category_service.get_categories()

@router_categories.post("", status_code=status.HTTP_201_CREATED)
def add_category(category: SCategoryAdd, category_service: CategoryService = Depends(get_category_service)) -> SCategoryRead:
    return category_service.add_category(category)

@router_categories.patch("/{category_id}")
def update_category(category_id: str, data: SCategoryUpdate, category_service: CategoryService = Depends(get_category_service)) -> SCategoryRead:
    updated_category = category_service.update_category(category_id, data)

    if updated_category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    return updated_category

@router_categories.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: str, category_service: CategoryService = Depends(get_category_service)) -> None:
    category_service.delete_category(category_id)
