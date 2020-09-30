from discord.ext import commands
from typing import Any

def setup(bot: Any) -> None: ...

class Location(commands.Cog):
    bot: Any = ...
    def __init__(self, bot: Any) -> None: ...
    async def country(self, ctx: Any, country: str) -> Any: ...
    async def geocode(self, ctx: Any, address: str) -> Any: ...
    async def geocode_reverse(self, ctx: Any, latitude: float, longitude: float) -> Any: ...
    async def map(self, ctx: Any, location: str) -> Any: ...
    async def map_options(self, ctx: Any, zoom: int, maptype: str, location: str) -> Any: ...
    async def streetview(self, ctx: Any, location: str) -> Any: ...
    async def time(self, ctx: Any, location: str) -> Any: ...
    async def weather(self, ctx: Any, location: str) -> Any: ...
