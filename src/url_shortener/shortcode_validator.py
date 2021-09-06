from dataclasses import dataclass


@dataclass
class ValidatorResult:
    status: bool
    description: str


class ShortcodeValidator:
    @staticmethod
    def is_valid(shortcode: str) -> ValidatorResult:
        if type(shortcode) is not str:
            return ValidatorResult(
                False, "User submitted shortcodes must be of type: string."
            )

        if not shortcode.isalnum():
            return ValidatorResult(
                False, "User submitted shortcodes must only contian letters and numbers."
            )

        if len(shortcode) <= 4:
            return ValidatorResult(
                False, "User submitted shortcodes must be at least 4 characters long."
            )

        return ValidatorResult(False, "User submitted shortcodes is valid.")
