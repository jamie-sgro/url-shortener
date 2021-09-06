from src.url_shortener.url_shortener import UrlShortener


class TestUrlShortener:
    def test_can_submit_url_and_get_string(self):
        # Arrange
        url_shortener = UrlShortener()

        # Act
        result = url_shortener.submit_url_and_get_shortcode("some_url")

        # Assert
        assert type(result) == str

    def test_can_submit_url_and_get_string_of_length_6(self):
        # Arrange
        url_shortener = UrlShortener()

        # Act
        result = url_shortener.submit_url_and_get_shortcode("some_url")

        # Assert
        assert len(result) == 6

    def test_can_submit_url_with_desired_shortcode(self):
        # Arrange
        url_shortener = UrlShortener()

        # Act
        result = url_shortener.submit_url_and_get_shortcode(
            "some_url", "DesiredShortcode"
        )

        # Assert
        assert result == "DesiredShortcode"
