import string
from random import choice

from src.database.i_db_accessor import DbAccessorResult, IDbAccessor
from src.url_shortener.shortcode_validator import ShortcodeValidator
from src.factory import Factory


class UrlShortener:
    db: IDbAccessor
    url: str
    shortcode: str

    def __init__(self) -> None:
        self.db = Factory.create_db_accessor()

    def submit_url_and_get_shortcode(self, url: str, user_shortcode: str = None) -> DbAccessorResult:
        self.url = url
        self.shortcode = self._get_shortcode(user_shortcode)
        result = self._send_shortcode_to_db()
        return result

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

    def _send_shortcode_to_db(self) -> DbAccessorResult:
        result = self.db.add("shortcodes", self.url, self.shortcode)
        return result
