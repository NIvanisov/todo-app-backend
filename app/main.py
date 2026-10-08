# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.task import router_tasks
from app.api.routers.category import router_categories
from app.core.config import get_settings
app = FastAPI()
settings = get_settings()

app.add_middleware(CORSMiddleware,
                   allow_origins=settings.cors_allowed_origins,
                   allow_methods=settings.cors_allowed_methods)

app.include_router(router_tasks)
app.include_router(router_categories)