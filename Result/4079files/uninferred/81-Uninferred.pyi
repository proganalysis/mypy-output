import requests
from .base import BaseHTTPUpdater
from typing import Any

logger: Any

class DuckDNSUpdater(BaseHTTPUpdater):
    _api_url: str = ...
    _domains: Any = ...
    _token: Any = ...
    info_code: Any = ...
    def __init__(self, domains: Any, token: Any, *args: Any, **kwargs: Any) -> None: ...
    def build_payload(self): ...
    def parse_result(self, response: requests.models.Response) -> Any: ...
