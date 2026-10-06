# app/cache/rediscache.py
from redis import Redis
import json

class RedisCache:

    def __init__(self, redis_url: str, cache_ttl_seconds: int | None = None) -> None:
        self.redis = Redis.from_url(redis_url, decode_responses=True)
        self.cache_ttl_seconds = cache_ttl_seconds

    def set(self, key: str, value: dict) -> None:
        self.redis.set(key, json.dumps(value), ex=self.cache_ttl_seconds)

    def get(self, key: str) -> dict:
        val = self.redis.get(key)
        if val is not None:
            return json.loads(val)

    def delete(self, key: str) -> None:
        self.redis.delete(key)