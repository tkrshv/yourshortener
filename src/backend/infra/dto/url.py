from dataclasses import dataclass


@dataclass
class UrlDTO:
    id: str
    original_url: str
    password: str | None = None
