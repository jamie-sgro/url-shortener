from typing import Final

from redis import Redis

from src.database.i_db_accessor import IDbAccessor
from src.factory import Factory

REDIS_HOST: Final = Factory.create_redis_host()


class DbAccessor(IDbAccessor):
    _redis: Redis()

    @classmethod
    def add(cls):
        ...

    @classmethod
    def query(cls):
        ...