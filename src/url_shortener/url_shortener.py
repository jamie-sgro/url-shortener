import string
from random import choice


class UrlShortener:
    @classmethod
    def submit_url_and_get_shortcode(
        cls, url: str, user_shortcode: str = None
    ) -> str:
        if user_shortcode is not None:
            cls._try_to_process_user_shortcode(user_shortcode)
            return user_shortcode

        return cls._random_string_of_length_n(6)

    @classmethod
    def _try_to_process_user_shortcode(cls, user_shortcode: str) -> str:
        if cls._shortcode_is_valid(user_shortcode):
            return user_shortcode
        raise NotImplementedError

    @staticmethod
    def _shortcode_is_valid() -> bool:
        ...

    @staticmethod
    def _random_string_of_length_n(n: int) -> str:
        return "".join(
            choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
            for i in range(n)
        )