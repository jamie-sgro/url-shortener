import string
from random import choice


class UrlShortener:
    @classmethod
    def submit_url_and_get_shortcode(
        cls, url: str, desired_shortcode: str = None
    ) -> str:
        if desired_shortcode is not None:
            return desired_shortcode
        return cls._random_string_of_length_n(6)

    @staticmethod
    def _random_string_of_length_n(n: int) -> str:
        return "".join(
            choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
            for i in range(n)
        )
