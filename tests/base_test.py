import pytest
from redis import Redis

from src.database.db_accessor import REDIS_HOST

class BaseTest:
    r: Redis

    @pytest.fixture(scope="function")
    def _setup_and_teardown_hashed_test_data(self):
        """
        - Initialize db connection
        - Only run tests if reserved keywords are not already in use
        - Remove all keywords from database after tests run (regardless of pass or fail)
        """
        self.r = Redis(REDIS_HOST)
        self.reserved_hashes = [("urls", "test"), ("users", "user123")]
        for hash, key in self.reserved_hashes:
            if self.r.hget(hash, key) is not None:
                raise AssertionError(f"redis key `{key}` already has data")
        yield
        for hash, key in self.reserved_hashes:
            self.r.hdel(hash, key)
