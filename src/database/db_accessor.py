from typing import Final

from redis import Redis

from src.database.i_db_accessor import IDbAccessor
from src.factory import Factory

REDIS_HOST: Final = Factory.create_redis_host()


class DbAccessor(IDbAccessor):
    _redis: Redis()

    @classmethod
    def __init(cls):
        cls._redis = Redis(REDIS_HOST)

    @classmethod
    def add(cls):
        cls.__init()

    @classmethod
    def query(cls):
        cls.__init()