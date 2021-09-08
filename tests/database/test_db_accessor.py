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
        self.reserved_hashes = [("urls", "test"), ("users", "user123")]
        for hash, key in self.reserved_hashes:
            if self.r.hget(hash, key) is not None:
                raise AssertionError(f"redis key `{key}` already has data")
        yield
        for hash, key in self.reserved_hashes:
            self.r.hdel(hash, key)
            self.r.hdel(key, hash)

    @pytest.mark.integration_test
    def test_can_add_data(self, _setup_and_teardown_hashed_test_data):
        # Arrange
        db = Factory.create_db_accessor()

        # Act
        result = db.add("users", "user123", "a user name")
        assert result.status
        assert result.value == "a user name"

    @pytest.mark.integration_test
    def test_cannot_add_same_data_twice(self, _setup_and_teardown_hashed_test_data):
        # Arrange
        db = Factory.create_db_accessor()

        # Act
        first_result = db.add("users", "user123", "a user name")
        second_result = db.add("users", "user123", "a user name")
        assert second_result.status == False

    @pytest.mark.integration_test
    def test_query_with_no_data_returns_false(
        self, _setup_and_teardown_hashed_test_data
    ):
        # Arrange
        db = Factory.create_db_accessor()

        result = db.query("urls", "test")

        assert result.value is None

    @pytest.mark.integration_test
    def test_can_increment_data_by_zero(self, _setup_and_teardown_hashed_test_data):
        # Arrange
        db = Factory.create_db_accessor()

        # Act
        result = db.increment("users", "user123", 0)
        assert result.status
        assert result.value != -1
        assert result.value == 0
        assert result.value != 1

    @pytest.mark.integration_test
    def test_can_increment_data_once(self, _setup_and_teardown_hashed_test_data):
        # Arrange
        db = Factory.create_db_accessor()

        # Act
        result = db.increment("users", "user123", 1)
        assert result.status
        assert result.value != 0
        assert result.value == 1
        assert result.value != 2

    @pytest.mark.integration_test
    def test_can_increment_data_several_times(
        self, _setup_and_teardown_hashed_test_data
    ):
        # Arrange
        db = Factory.create_db_accessor()

        # Act
        result = db.increment("users", "user123", 1)
        result = db.increment("users", "user123", 1)
        result = db.increment("users", "user123", 1)
        assert result.status
        assert result.value != 0
        assert result.value == 3
        assert result.value != 2

    @pytest.mark.integration_test
    def test_can_increment_data_by_different_values(
        self, _setup_and_teardown_hashed_test_data
    ):
        # Arrange
        db = Factory.create_db_accessor()

        # Act
        result = db.increment("users", "user123", 0)
        result = db.increment("users", "user123", 1)
        assert result.status
        assert result.value != 0
        assert result.value == 1
        assert result.value != 2
