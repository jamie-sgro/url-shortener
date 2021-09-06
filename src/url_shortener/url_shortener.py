import string
from random import choice

from src.database.i_db_accessor import DbAccessorResult, IDbAccessor
from src.url_shortener.shortcode_validator import ShortcodeValidator, ShortcodeResult
from src.factory import Factory


class UrlShortener:
    db: IDbAccessor
    url: str
    shortcode: str

    def __init__(self) -> None:
        self.db = Factory.create_db_accessor()

    def submit_url_and_get_shortcode(self, url: str, user_shortcode: str = None) -> DbAccessorResult:
        self.url = url
        shortcode_model = self._get_shortcode(user_shortcode)
        if not shortcode_model.value:
            return DbAccessorResult(False, shortcode_model.description)
        self.shortcode = shortcode_model.value
        return self._send_shortcode_to_db()

    @classmethod
    def _get_shortcode(cls, user_shortcode: str = None) -> ShortcodeResult:
        if user_shortcode is not None:
            return ShortcodeValidator.is_valid(user_shortcode)
        random_shortcode = cls._random_string_of_length_n(6)
        return ShortcodeResult(True, "Random shortcode used", random_shortcode)

    @staticmethod
    def _random_string_of_length_n(n: int) -> str:
        return "".join(
            choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
            for i in range(n)
        )

    def _send_shortcode_to_db(self) -> DbAccessorResult:
        result = self.db.add("shortcodes", self.url, self.shortcode)
        # Because the db currently being used is redis, the in-memory lookup costs are 
        # low enough to simply include the reverse value-key
        self.db.add("urls", self.shortcode, self.url)
        return result

    def get_url_from_shortcode(self, shortcode: str) -> DbAccessorResult:
        return self.db.query("urls", shortcode)