from dataclasses import dataclass
from datetime import datetime


@dataclass
class UrlViewDTO:
    id: str
    created_at: datetime
    