from typing import Any

bot: Any
cs: Any
chan: Any

async def on_connect() -> None: ...
async def youtube_info(message: Any) -> None: ...
async def quit(message: Any) -> None: ...
async def join(message: Any) -> None: ...
async def part(message: Any) -> None: ...
async def greet(channel: Any) -> None: ...
async def ping(): ...
async def cli_input() -> None: ...

loop: Any
