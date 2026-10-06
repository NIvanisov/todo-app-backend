# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.task import router
from app.databases.database import lifespan
from app.core.config import get_settings

app = FastAPI(lifespan=lifespan)
settings = get_settings()

app.add_middleware(CORSMiddleware,
                   allow_origins=settings.cors_allowed_origins,
                   allow_methods=settings.cors_allowed_methods)

app.include_router(router)