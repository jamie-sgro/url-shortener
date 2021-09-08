from typing import Any, Final

from redis import StrictRedis

from src.database.i_db_accessor import IDbAccessor, DbAccessorResult

REDIS_HOST: Final = "redis"


class DbAccessor(IDbAccessor):
    _redis: StrictRedis

    @classmethod
    def __init(cls):
        cls._redis = StrictRedis(REDIS_HOST, decode_responses=True)

    @classmethod
    def add(cls, name: str, key: str, value: Any) -> DbAccessorResult:
        cls.__init()
        if cls._redis.hget(name, key) is not None:
            return DbAccessorResult(
                False, f"The key `{key}` already exists in the database"
            )
        cls._redis.hset(name, key, value)
        return DbAccessorResult(True, "Success", value)

    @classmethod
    def add_overwrite(cls, name: str, key: str, value: Any) -> DbAccessorResult:
        cls.__init()
        cls._redis.hset(name, key, value)
        return DbAccessorResult(True, "Success", value)

    @classmethod
    def add_complex(cls, name: str, mapping: dict) -> DbAccessorResult:
        """Set key to value within hash name for each corresponding key
        and value from the mapping dict"""
        cls.__init()
        result = cls._redis.hmset(name, mapping)
        return DbAccessorResult(True, "Success", mapping)

    @classmethod
    def increment(cls, name: str, key: str, value: int) -> DbAccessorResult:
        """Increments the number stored at key by one. If the key does not exist,
        it is set to 0 before performing the operation"""
        cls.__init()
        result = cls._redis.hincrby(name, key, value)
        return DbAccessorResult(True, "Success", result)

    @classmethod
    def query(cls, name: str, key: str) -> DbAccessorResult:
        cls.__init()
        result = cls._redis.hget(name, key)  # type: ignore
        if result is None:
            return DbAccessorResult(
                False, f"The shortcode `{key}` does not exist in the database"
            )
        return DbAccessorResult(True, "Success", result)
