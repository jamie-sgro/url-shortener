from typing import Final

from redis import Redis

from src.factory import Factory

REDIS_HOST: Final = Factory.create_redis_host()


class DbAccessor:
    _redis: Redis()
