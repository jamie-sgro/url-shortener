import pytest
from redis import Redis

from src.url_shortener.url_shortener import UrlShortener
from src.database.db_accessor import REDIS_HOST


class TestUrlShortener:
    r: Redis

    @pytest.fixture(scope="function")
    def _setup_and_teardown_hashed_test_data(self):
        """
        - Initialize db connection
        - Only run tests if reserved keywords are not already in use
        - Remove all keywords from database after tests run (regardless of pass or fail)
        """
        self.r = Redis(REDIS_HOST)
        self.reserved_hashes = [("shortcodes", "test"), ("urls", "Abc123")]
        for hash, key in self.reserved_hashes:
            if self.r.hget(hash, key) is not None:
                raise AssertionError(f"redis key `{hash}:{key}` already has data")
        yield
        for hash, key in self.reserved_hashes:
            self.r.hdel(hash, key)

    @pytest.mark.integration_test
    def test_can_lookup_url_from_shortcode(self, _setup_and_teardown_hashed_test_data):
        # Arrange
        url_shortener = UrlShortener()
        url = "test"
        shortcode = "Abc123"

        # Act
        shortcode_model = url_shortener.submit_url_and_get_shortcode(url, "Abc123")
        assert shortcode_model.status == True, shortcode_model.description
        assert type(shortcode_model.value) == str
        shortcode = str(shortcode_model.value)
        result = url_shortener.get_url_from_shortcode(shortcode)

        # Assert
        assert result.value == str.encode(url)
