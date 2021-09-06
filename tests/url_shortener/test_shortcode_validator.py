from src.url_shortener.shortcode_validator import ShortcodeValidator


class TestShortcodeValidator:
    def test_not_of_type_string_invalid(self):
        assert ShortcodeValidator.is_valid(123).status == False  # type: ignore
        assert ShortcodeValidator.is_valid(123456789).status == False  # type: ignore
        assert ShortcodeValidator.is_valid(1.23).status == False  # type: ignore
        assert ShortcodeValidator.is_valid(["abcd"]).status == False  # type: ignore
        assert ShortcodeValidator.is_valid(["abcd", "efgh"]).status == False  # type: ignore
        assert ShortcodeValidator.is_valid(("abcd", "efgh")).status == False  # type: ignore

    def test_short_strings_invalid(self):
        assert ShortcodeValidator.is_valid("123").status == False
        assert ShortcodeValidator.is_valid("abc").status == False
