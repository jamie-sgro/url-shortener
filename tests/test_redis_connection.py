from typing import Final
from redis import Redis

REDIS_HOST: Final = "redis"

class TestRedisConnection:
    def test_ping_is_true(self):
        r = Redis(REDIS_HOST, socket_connect_timeout=1)  # short timeout for the test
        r.ping()