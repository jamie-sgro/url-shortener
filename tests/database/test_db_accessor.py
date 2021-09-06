import pytest
from redis import Redis

from src.database.db_accessor import REDIS_HOST
from src.factory import Factory
from tests.base_test import BaseTest


class TestRedisConnection(BaseTest):
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
    def test_query_with_no_data_returns_false(self, _setup_and_teardown_hashed_test_data):
        # Arrange
        db = Factory.create_db_accessor()

        result = db.query("url", "test")

        assert result.value is None

    @pytest.mark.integration_test
    def test_can_add_and_query_data(self, _setup_and_teardown_hashed_test_data):
        # Arrange
        db = Factory.create_db_accessor()

        # Act
        db.add("users", "user123", "a user name")

        # Assert
        result = db.query("users", "user123")
        assert result.status
        assert result.value == b"a user name"