from blueman.Service import Service
from typing import Any, Optional

class NetworkService(Service):
    _service: Any = ...
    def __init__(self, device: Any, uuid: Any) -> None: ...
    @property
    def available(self): ...
    @property
    def connected(self): ...
    def connect(self, reply_handler: Optional[Any] = ..., error_handler: Optional[Any] = ...) -> None: ...
    def disconnect(self, reply_handler: Optional[Any] = ..., error_handler: Optional[Any] = ..., *args: Any) -> None: ...
