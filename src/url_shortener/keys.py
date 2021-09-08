from dataclasses import dataclass


@dataclass
class Keys:
    """Single location for all column names / keys in key-value pairs"""
    urls: str = "urls"
    shortcodes: str = "shortcodes"
    date_registered: str = "date_registered"
    last_accessed: str = "last_accessed"
    access_count: str = "access_count"

    def stats(self, shortcode: str):
        """ Current namespace for stats related to a shortcode"""
        return f"{shortcode}-stats"
