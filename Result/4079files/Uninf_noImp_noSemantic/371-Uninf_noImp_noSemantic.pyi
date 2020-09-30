import discord
from pcbot import utils
from typing import Any

client: discord.Client
twitch_config: Any

async def twitch_group(message: discord.Message, _: utils.placeholder) -> Any: ...
async def notify_channels(message: discord.Message, *channels: discord.Channel) -> Any: ...
def make_twitch_embed(member: discord.Member, response: dict) -> Any: ...
def started_streaming(before: discord.Member, after: discord.Member) -> Any: ...
async def on_member_update(before: discord.Member, after: discord.Member) -> Any: ...
