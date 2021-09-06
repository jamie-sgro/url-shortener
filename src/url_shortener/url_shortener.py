import string
from random import choice

from src.url_shortener.shortcode_validator import ShortcodeValidator


class UrlShortener:
    url: str
    shortcode: str

    @classmethod
    def submit_url_and_get_shortcode(cls, url: str, user_shortcode: str = None) -> str:
        cls.url = url
        cls.shortcode = cls._get_shortcode(user_shortcode)
        cls._send_shortcode_to_db()
        return cls.shortcode

    @classmethod
    def _get_shortcode(cls, user_shortcode: str = None) -> str:
        shortcode: str
        if user_shortcode is not None:
            cls._try_to_process_user_shortcode(user_shortcode)
            shortcode = user_shortcode
        else:
            shortcode = cls._random_string_of_length_n(6)
        return shortcode

    @classmethod
    def _try_to_process_user_shortcode(cls, user_shortcode: str) -> str:
        if ShortcodeValidator.is_valid(user_shortcode).status:
            return user_shortcode
        raise NotImplementedError

    @staticmethod
    def _random_string_of_length_n(n: int) -> str:
        return "".join(
            choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
            for i in range(n)
        )

    @classmethod
    def _send_shortcode_to_db(cls):
        # TODO: Send to db
        return cls.shortcode
