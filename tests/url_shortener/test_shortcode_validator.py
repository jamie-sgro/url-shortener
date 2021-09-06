from src.url_shortener.shortcode_validator import ShortcodeValidator


class TestShortcodeValidator:
    def test_short_strings_invalid(self):
        assert ShortcodeValidator.is_valid("123").status == False
