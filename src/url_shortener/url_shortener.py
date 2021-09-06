from typing import List
import string
from random import choice
from datetime import datetime, timezone

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
        # Because the db currently being used is redis, the in-memory lookup costs are 
        # low enough to simply include the reverse value-key
        self.db.add("urls", self.shortcode, self.url)
        result = self.db.add("shortcodes", self.url, self.shortcode)

        self.db.add("date_registered", self.shortcode, self._get_utc_now())

        return result

    def get_url_from_shortcode(self, shortcode: str) -> DbAccessorResult:
        shortcode_model = ShortcodeValidator.is_valid(shortcode)
        print(shortcode_model, flush=True)
        if not shortcode_model.status:
            return DbAccessorResult(False, shortcode_model.description)
        
        self.db.add_overwrite("last_accessed", shortcode, self._get_utc_now())

        return self.db.query("urls", shortcode)

    @staticmethod
    def _get_utc_now() -> str:
        return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    def get_stats_from_shortcode(self, shortcode: str) -> DbAccessorResult:
        shortcode_model = ShortcodeValidator.is_valid(shortcode)
        if not shortcode_model.status:
            return DbAccessorResult(False, shortcode_model.description)
        
        stats: List[DbAccessorResult] = []
        stats.append(self._get_date_registered(shortcode))
        stats.append(self._get_last_accessed(shortcode))

        result = self._combine_db_results(stats)

        return result

    def _get_date_registered(self, shortcode: str) -> DbAccessorResult:
        db_model = self.db.query("date_registered", shortcode)
        db_model.value = f"date registered: {db_model.value}"
        return db_model

    def _get_last_accessed(self, shortcode: str) -> DbAccessorResult:
        db_model = self.db.query("last_accessed", shortcode)
        db_model.value = f"last accessed: {db_model.value}"
        return db_model

    def _combine_db_results(self, results: List[DbAccessorResult]) -> DbAccessorResult:
        for result in results:
            if not result.status:
                return result

        concatenated_values = ""
        for result in results:
            concatenated_values += "\n" + str(result.value)

        return DbAccessorResult(True, "Success", concatenated_values)