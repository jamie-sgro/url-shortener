from typing import Any, Final

from redis import Redis

from src.database.i_db_accessor import IDbAccessor, DbAccessorResult

REDIS_HOST: Final = "redis"


class DbAccessor(IDbAccessor):
    _redis: Redis

    @classmethod
    def __init(cls):
        cls._redis = Redis(REDIS_HOST)

    @classmethod
    def add(cls, name: str, key: str, value: Any) -> DbAccessorResult:
        cls.__init()
        if cls._redis.hget(name, key) is not None:
            return DbAccessorResult(False, f"redis key `{key}` already has a value")
        cls._redis.hset(name, key, value)
        return DbAccessorResult(True, "Success", value)

    @classmethod
    def query(cls, name: str, key: str) -> DbAccessorResult:
        cls.__init()
        result = cls._redis.hget(name, key)  # type: ignore
        return DbAccessorResult(True, "Success", result)
