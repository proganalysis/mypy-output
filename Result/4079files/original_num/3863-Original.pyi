# (generated with --quick)

import asyncio.events
from typing import Any, Coroutine, Optional

Forbidden: Any
InvalidArgument: Any
asyncio: module
checks: Any
commands: Any
discordutils: Any
json: module
linkutils: Any
os: module
twitconn: Any
twitutils: Any

class Streams:
    blacklist: Any
    bot: Any
    destinations: Any
    kill: Any
    loop: Optional[asyncio.events.AbstractEventLoop]
    reboot: Any
    restart: Any
    slist: Any
    stalk: Any
    stop_loop: bool
    def __init__(self, bot) -> None: ...
    def add_channel(self, user, channel_id) -> bool: ...
    def blacklist_channel(self, channel_id) -> bool: ...
    def end(self) -> Coroutine[Any, Any, None]: ...
    def get_stalks(self) -> list: ...
    def kill_stream(self) -> Coroutine[Any, Any, None]: ...
    def reboot_stream(self) -> Coroutine[Any, Any, None]: ...
    def restart_stream(self) -> Coroutine[Any, Any, None]: ...
    def start(self) -> Coroutine[Any, Any, None]: ...
    def stream(self) -> Coroutine[Any, Any, None]: ...
    def tweet_retriever(self) -> Coroutine[Any, Any, nothing]: ...
    def update_json(self) -> None: ...

def setup(bot) -> None: ...