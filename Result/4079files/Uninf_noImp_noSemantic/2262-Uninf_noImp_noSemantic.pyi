import asyncio
from typing import Any

ratelimit_key_queue_map: Any
ratelimit_key_time_map: Any

def _get_float(data: Any, default: Any): ...
def _get_int(data: Any, default: Any): ...
async def basic_request(loop: asyncio.AbstractEventLoop, api_key: str, timeout_seconds: float, endpoint: str, *args: Any, method: str=..., handle_ratelimiting: bool=..., _cur_retry: int=..., **kwargs: Any) -> Any: ...
def _add_request_parameters(func: Any): ...
async def get_platforms(*args: Any, api_key: str, loop: asyncio.AbstractEventLoop, api_version: int=..., **kwargs: Any) -> Any: ...
async def get_playlists(*args: Any, api_key: str, loop: asyncio.AbstractEventLoop, api_version: int=..., **kwargs: Any) -> Any: ...
async def get_seasons(*args: Any, api_key: str, loop: asyncio.AbstractEventLoop, api_version: int=..., **kwargs: Any) -> Any: ...
async def get_tiers(*args: Any, api_key: str, loop: asyncio.AbstractEventLoop, api_version: int=..., **kwargs: Any) -> Any: ...
async def get_ranked_leaderboard(playlist_id: int, *args: Any, api_key: str, loop: asyncio.AbstractEventLoop, api_version: int=..., **kwargs: Any) -> Any: ...
async def get_stats_leaderboard(stat_type: str, *args: Any, api_key: str, loop: asyncio.AbstractEventLoop, api_version: int=..., **kwargs: Any) -> Any: ...
async def get_player(unique_id: str, platform_id: int, *args: Any, api_key: str, loop: asyncio.AbstractEventLoop, api_version: int=..., **kwargs: Any) -> Any: ...
async def get_player_batch(unique_id_platform_pairs: tuple, *args: Any, api_key: str, loop: asyncio.AbstractEventLoop, api_version: int=..., **kwargs: Any) -> Any: ...
async def search_players(display_name: str, page: int, *args: Any, api_key: str, loop: asyncio.AbstractEventLoop, api_version: int=..., **kwargs: Any) -> Any: ...
