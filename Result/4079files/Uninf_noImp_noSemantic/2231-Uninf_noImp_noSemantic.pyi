from .dispatcher import SlackDispatcher
from typing import Any

logger: Any

class ActionDispatcher(SlackDispatcher):
    _token: Any = ...
    def __init__(self, http_client: Any, users: Any, channels: Any, groups: Any, plugins: Any, save: Any, loop: Any, token: Any) -> None: ...
    async def _incoming(self, request: Any): ...
    def register(self, id_: Any, func: Any, public: bool = ...) -> None: ...
