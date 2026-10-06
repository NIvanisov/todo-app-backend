# core/config.py
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    DATABASE_URL: str
    cors_allowed_origins: list[str]
    cors_allowed_methods: list[str]

def get_settings():
    return Settings(
        DATABASE_URL=os.getenv("DATABASE_URL"),
        cors_allowed_origins=[os.getenv("CORS_ORIGINS")],
        cors_allowed_methods=[os.getenv("CORS_METHODS")]
    )