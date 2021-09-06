from typing import Final

from redis import Redis

from src.database.i_db_accessor import IDbAccessor

REDIS_HOST: Final = "redis"


class DbAccessor(IDbAccessor):
    _redis: Redis()

    @classmethod
    def __init(cls):
        cls._redis = Redis(REDIS_HOST)

    @classmethod
    def add(cls, name: str, key: str):
        cls.__init()

    @classmethod
    def query(cls, name: str, key: str):
        cls.__init()
