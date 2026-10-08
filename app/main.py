# main.py
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from collections.abc import Callable
from time import perf_counter
from itertools import count
import logging

from app.api.routers.task import router_tasks
from app.api.routers.category import router_categories
from app.core.config import get_settings
from app.core.logging import configure_logging

app = FastAPI()
settings = get_settings()
configure_logging()
logger = logging.getLogger("app.middleware")
count_of_requests = count(1)

app.add_middleware(CORSMiddleware,
                   allow_origins=settings.cors_allowed_origins,
                   allow_methods=settings.cors_allowed_methods)

@app.middleware("http")
async def log_requests(request: Request, call_next: Callable) -> Response:
    start_at = perf_counter()
    try:
        response = await call_next(request)
    except Exception:
        logger.exception(
            "Request failed: %s %s completed_in=%.2fms",
            request.method,
            request.url.path,
            (perf_counter() - start_at) * 1000,
        )
        raise

    response.headers["x-request-number"] = str(next(count_of_requests))
    logger.info(
        "Request done: %s %s -> %s (%.2fms)",
        request.method,
        request.url.path,
        response.status_code,
        (perf_counter() - start_at) * 1000
    )
    return response

app.include_router(router_tasks)
app.include_router(router_categories)