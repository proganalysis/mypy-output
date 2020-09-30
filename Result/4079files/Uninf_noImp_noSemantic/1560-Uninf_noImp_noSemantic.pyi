import aiohttp
from typing import Any, Optional

class CustomClientResponse(aiohttp.ClientResponse):
    headers: Any = ...
    raw_headers: Any = ...
    async def start(self, connection: Any, read_until_eof: bool = ...): ...

class BaseDriver:
    timeout: Any = ...
    _loop: Any = ...
    def __init__(self, timeout: int = ..., loop: Optional[Any] = ...) -> None: ...
    async def json(self, url: Any, params: Any, timeout: Optional[Any] = ...) -> None: ...
    async def get_text(self, url: Any, params: Any, timeout: Optional[Any] = ...) -> None: ...
    async def get_bin(self, url: Any, params: Any, timeout: Optional[Any] = ...) -> None: ...
    async def post_text(self, url: Any, data: Any, timeout: Optional[Any] = ...) -> None: ...
    async def close(self) -> None: ...

class HttpDriver(BaseDriver):
    session: Any = ...
    def __init__(self, timeout: int = ..., loop: Optional[Any] = ..., session: Optional[Any] = ...) -> None: ...
    async def json(self, url: Any, params: Any, timeout: Optional[Any] = ...): ...
    async def get_text(self, url: Any, params: Any, timeout: Optional[Any] = ...): ...
    async def get_bin(self, url: Any, params: Any, timeout: Optional[Any] = ...): ...
    async def post_text(self, url: Any, data: Any, timeout: Optional[Any] = ...): ...
    async def close(self) -> None: ...

class Socks5Driver(HttpDriver):
    connector: Any = ...
    session: Any = ...
    def __init__(self, address: Any, port: Any, login: Optional[Any] = ..., password: Optional[Any] = ..., timeout: int = ..., loop: Optional[Any] = ...) -> None: ...