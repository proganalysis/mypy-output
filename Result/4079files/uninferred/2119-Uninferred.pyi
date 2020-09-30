from discord.ext import commands
from typing import Any, Optional

class Generic(commands.Cog):
    GOT_AIR_DATE: Any = ...
    GOT_LOGO: str = ...
    bot: Any = ...
    blue: Any = ...
    def __init__(self, bot: Any) -> None: ...
    async def say(self, ctx: Any, message: Any) -> None: ...
    async def ball(self, ctx: Any, *, query: Optional[Any] = ...): ...
    async def same(self, ctx: Any) -> None: ...
    async def unsame(self, ctx: Any) -> None: ...
    async def resame(self, ctx: Any) -> None: ...
    async def slap(self, ctx: Any, *, target: Optional[Any] = ...): ...
    async def report(self, ctx: Any) -> None: ...
    async def love(self, ctx: Any, *, target: Optional[Any] = ...): ...
    async def aesthetify(self, ctx: Any, a_text: Any) -> None: ...
    async def uptime(self, ctx: Any) -> None: ...
    async def ping(self, ctx: Any) -> None: ...
    async def about(self, ctx: Any) -> None: ...

def setup(bot: Any) -> None: ...
