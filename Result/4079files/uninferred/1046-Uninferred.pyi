from typing import Any

class ChandereError(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

def check_http_status(code: int, url: Any=...) -> Any: ...