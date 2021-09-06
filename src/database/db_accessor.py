from typing import Any, Final

from redis import Redis

from src.database.i_db_accessor import IDbAccessor

REDIS_HOST: Final = "redis"


class DbAccessor(IDbAccessor):
    _redis: Redis

    @classmethod
    def __init(cls):
        cls._redis = Redis(REDIS_HOST)

    @classmethod
    def add(cls, name: str, key: str, value: Any):
        cls.__init()
        cls._redis.hset(name, key, value)

    @classmethod
    def query(cls, name: str, key: str) -> bytes:
        cls.__init()
        return cls._redis.hget(name, key) # type: ignore
