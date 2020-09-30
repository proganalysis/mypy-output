from typing import Any

class General:
    bot: Any = ...
    def __init__(self, bot: Any) -> None: ...
    async def load(self, ctx: Any, extension_name: str) -> Any: ...
    async def unload(self, ctx: Any, extension_name: str) -> Any: ...
    async def hello(self, ctx: Any) -> None: ...
    async def carlito(self) -> None: ...
    async def eightball(self, ctx: Any, question: str) -> Any: ...
    async def roll(self, dice: str) -> Any: ...
    async def join(self, ctx: Any, role: str) -> Any: ...
    async def leave(self, ctx: Any, role: str) -> Any: ...
    async def register(self, ctx: Any) -> None: ...
    async def serverinfo(self, ctx: Any): ...

def setup(bot: Any) -> None: ...
