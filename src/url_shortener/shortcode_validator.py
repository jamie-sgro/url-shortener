from dataclasses import dataclass
from typing import Union


@dataclass
class ShortcodeResult:
    status: bool
    description: str
    value: Union[str, None] = None


class ShortcodeValidator:
    @staticmethod
    def is_valid(shortcode: str) -> ShortcodeResult:
        if type(shortcode) is not str:
            return ShortcodeResult(
                False, "User submitted shortcodes must be of type: string."
            )

        if not shortcode.isalnum():
            return ShortcodeResult(
                False,
                "User submitted shortcodes must only contian letters and numbers.",
            )

        if len(shortcode) <= 4:
            return ShortcodeResult(
                False, "User submitted shortcodes must be at least 4 characters long."
            )

        return ShortcodeResult(True, "User submitted shortcode is valid.", shortcode)
