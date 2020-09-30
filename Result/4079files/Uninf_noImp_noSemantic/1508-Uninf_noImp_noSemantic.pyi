import discord
from typing import Any

client: discord.Client
wordsearch: Any
wordsearch_words: Any
tutorial: str
character_match: str
word_list_url: str

def valid_word(message: discord.Message) -> Any: ...
def valid_guess(message: discord.Message) -> Any: ...
def format_hint(hint: Any): ...
async def auto_word(count: int = ...): ...
def stop_wordsearch(channel: discord.Channel) -> Any: ...
async def start_wordsearch(channel: discord.Channel, host: discord.Member, word: str=...) -> Any: ...
async def wordsearch_(message: discord.Message) -> Any: ...
async def auto(message: discord.Message, count: int=...) -> Any: ...
async def on_reload(name: str) -> Any: ...