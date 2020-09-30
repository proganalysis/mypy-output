from discord.ext import commands
from typing import Any, Optional

def setup(bot: Any) -> None: ...

class Words(commands.Cog):
    bot: Any = ...
    def __init__(self, bot: Any) -> None: ...
    async def antonym(self, ctx: Any, word: str) -> Any: ...
    async def define(self, ctx: Any, word: str) -> Any: ...
    async def pronunciation(self, ctx: Any, word: str) -> Any: ...
    async def rhyme(self, ctx: Any, word: str) -> Any: ...
    async def spellcheck(self, ctx: Any, words: str) -> Any: ...
    async def synonym(self, ctx: Any, word: str) -> Any: ...
    async def translate(self, ctx: Any, text: str) -> Any: ...
    async def translate_from(self, ctx: Any, from_language_code: str, to_language_code: str, text: str) -> Any: ...
    async def translate_languages(self, ctx: Any, language_code: str=...) -> Any: ...
    async def translate_to(self, ctx: Any, language_code: str, text: str) -> Any: ...
    async def process_translate(self, ctx: Any, text: Any, to_language_code: Any, from_language_code: Optional[Any] = ...): ...
