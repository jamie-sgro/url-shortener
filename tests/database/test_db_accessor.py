import pytest
from redis import Redis

from src.database.db_accessor import REDIS_HOST
from src.factory import Factory

class TestRedisConnection:
    r: Redis

    @pytest.fixture(scope="function")
    def _setup_and_teardown_hashed_test_data(self):
        """
        - Initialize db connection
        - Only run tests if reserved keywords are not already in use
        - Remove all keywords from database after tests run (regardless of pass or fail)
        """
        self.r = Redis(REDIS_HOST)
        self.reserved_hashes = [("url", "test"), ("users", "user123")]
        for hash, key in self.reserved_hashes:
            if self.r.hget(hash, key) is not None:
                raise AssertionError(f"redis key `{key}` already has data")
        yield
        for hash, key in self.reserved_hashes:
            self.r.hdel(hash, key)

    @pytest.mark.integration_test
    def test_can_add_data(self, _setup_and_teardown_hashed_test_data):
        # Arrange
        db = Factory.create_db_accessor()

        # Act
        db.add("users", "user123", "a user name")

    @pytest.mark.integration_test
    def test_can_add_and_query_data(self, _setup_and_teardown_hashed_test_data):
        # Arrange
        db = Factory.create_db_accessor()

        # Act
        db.add("users", "user123", "a user name")

        # Assert
        result = db.query("users", "user123")
        assert result == b"a user name"
