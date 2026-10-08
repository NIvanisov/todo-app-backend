# core/config.py
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    DATABASE_URL: str
    redis_url: str
    cache_ttl_seconds: int
    cache_tasks_key: str
    cors_allowed_origins: list[str]
    cors_allowed_methods: list[str]

def get_settings():
    return Settings(
        DATABASE_URL=os.getenv("DATABASE_URL"),
        redis_url=os.getenv("REDIS_URL"),
        cache_ttl_seconds=int(os.getenv("CACHE_TTL_SECONDS")),
        cache_tasks_key=os.getenv("CACHE_TASKS_KEY"),
        cors_allowed_origins=os.getenv("CORS_ORIGINS").split(","),
        cors_allowed_methods=os.getenv("CORS_METHODS").split(",")
    )