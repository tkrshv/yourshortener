from fastapi import HTTPException


class NotFoundUrlError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Url not found")


class UrlPasswordError(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Invalid password")


class UrlIdExists(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Url with this ID exists")


class UrlCantChanged(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="This url can`t be changed")
