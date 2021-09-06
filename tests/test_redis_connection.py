from typing import Final

import pytest
from redis import Redis

from src.factory import Factory

REDIS_HOST: Final = Factory.create_redis_host()


class TestRedisConnection:
    @pytest.mark.integration_test
    def test_can_ping_database(self):
        r = Redis(REDIS_HOST, socket_connect_timeout=1)  # short timeout for the test
        r.ping()
