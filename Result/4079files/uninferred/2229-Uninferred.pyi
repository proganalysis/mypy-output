from Cogs import DisplayName as DisplayName, Nullify as Nullify
from discord.ext import commands
from typing import Any, Optional

def setup(bot: Any) -> None: ...

class Spooktober(commands.Cog):
    bot: Any = ...
    settings: Any = ...
    def __init__(self, bot: Any, settings: Any) -> None: ...
    async def message(self, message: Any) -> None: ...
    async def spooking(self, ctx: Any, *, yes_no: Optional[Any] = ...) -> None: ...
