from hashlib import md5
import random


def formatting_url(url: str, length: int) -> str:
    digest = md5(url.encode()).hexdigest()
    return "".join(random.choices(digest, k=length))
