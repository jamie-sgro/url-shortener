from typing import List
import string
from random import choice
from datetime import datetime, timezone

from src.database.i_db_accessor import DbAccessorResult, IDbAccessor
from src.url_shortener.shortcode_validator import ShortcodeValidator, ShortcodeResult
from src.factory import Factory


class UrlShortener:
    db: IDbAccessor

    def __init__(self) -> None:
        self.db = Factory.create_db_accessor()

    def submit_url_and_get_shortcode(
        self, url: str, user_shortcode: str = None
    ) -> DbAccessorResult:
        self.url = url
        shortcode_model = self._get_shortcode(user_shortcode)
        if not shortcode_model.value:
            return DbAccessorResult(False, shortcode_model.description)
        shortcode = shortcode_model.value
        return self._send_shortcode_to_db(url, shortcode)

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

    def _send_shortcode_to_db(self, url: str, shortcode: str) -> DbAccessorResult:
        # Because the db currently being used is redis, the in-memory lookup costs are
        # low enough to simply include the reverse value-key
        self.db.add("urls", shortcode, self.url)
        result = self.db.add("shortcodes", url, shortcode)

        self._add_stats(shortcode)

        return result

    def _add_stats(self, shortcode):
        stats = {
            "date_registered": self._get_utc_now(),
            "last_accessed": "never",
            "access_count": 0,
        }
        self.db.add_complex(f"{shortcode}-stats", stats)

    def get_url_from_shortcode(self, shortcode: str) -> DbAccessorResult:
        shortcode_model = ShortcodeValidator.is_valid(shortcode)
        if not shortcode_model.status:
            return DbAccessorResult(False, shortcode_model.description)

        stats_key = f"{shortcode}-stats"

        self.db.add_overwrite(stats_key, "last_accessed", self._get_utc_now())
        self.db.increment(stats_key, "access_count", 1)

        return self.db.query("urls", shortcode)

    @staticmethod
    def _get_utc_now() -> str:
        return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    def get_stats_from_shortcode(self, shortcode: str) -> DbAccessorResult:
        shortcode_model = ShortcodeValidator.is_valid(shortcode)
        if not shortcode_model.status:
            return DbAccessorResult(False, shortcode_model.description)

        return self.db.query_all(f"{shortcode}-stats")
