from typing import Any
from src.database.i_db_accessor import DbAccessorResult, IDbAccessor

from src.url_shortener.url_shortener import UrlShortener


class TestUrlShortener:
    class MockDb(IDbAccessor):
        @classmethod
        def add(cls, name: str, key: str, value: Any) -> DbAccessorResult:
            return DbAccessorResult(True, "Success", value)

        @classmethod
        def add_overwrite(cls, name: str, key: str, value: Any) -> DbAccessorResult:
            return DbAccessorResult(True, "Success", value)

        @classmethod
        def increment(cls, name: str, key: str, value: int) -> DbAccessorResult:
            return DbAccessorResult(True, "Success", value) 

        @classmethod
        def query(cls, name: str, key: str) -> DbAccessorResult:
            return DbAccessorResult(True, "Success", "a_value")

    def test_can_submit_url_and_get_string(self):
        # Arrange
        url_shortener = UrlShortener()
        url_shortener.db = self.MockDb()

        # Act
        result = url_shortener.submit_url_and_get_shortcode("some_url")

        # Assert
        assert type(result.value) == str

    def test_can_submit_url_and_get_string_of_length_6(self):
        # Arrange
        url_shortener = UrlShortener()
        url_shortener.db = self.MockDb()

        # Act
        result = url_shortener.submit_url_and_get_shortcode("some_url")

        # Assert
        assert type(result.value) == str
        result.value = str(result.value)
        assert len(result.value) == 6

    def test_can_submit_url_with_desired_shortcode(self):
        # Arrange
        url_shortener = UrlShortener()
        url_shortener.db = self.MockDb()

        # Act
        result = url_shortener.submit_url_and_get_shortcode(
            "some_url", "DesiredShortcode"
        )

        # Assert
        assert result.value == "DesiredShortcode"
