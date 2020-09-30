import asyncio
from rain.cythons.form import MultiDict
from rain.cythons.tcpio import TCPIo
from typing import Any

_loop: Any

def get_loop(): ...
def set_loop(loop: asyncio.AbstractEventLoop) -> Any: ...

class RequestTimeoutException(Exception): ...

class Environment:
    query: Any = ...
    data: Any = ...
    headers: Any = ...
    def __init__(self, query: MultiDict=..., data: Any=..., headers: MultiDict=...) -> None: ...
    def copy(self): ...

class ClientResponse:
    status: int = ...
    reason: str = ...
    header: Any = ...
    _body: Any = ...
    cookies: Any = ...
    def __init__(self) -> None: ...
    @property
    def json(self): ...
    @property
    def txt(self): ...
    @property
    def raw(self): ...

async def fetch(method: str, url: str, query: dict=..., data: Any=..., headers: dict=..., env: Environment=..., loop: asyncio.AbstractEventLoop=..., timeout: float=...) -> ClientResponse: ...
async def _task_wrapper(future: Any, conn: Any) -> None: ...
def _timeout_handler(future: Any, task: Any) -> None: ...
async def _read_response(conn: TCPIo) -> Any: ...
