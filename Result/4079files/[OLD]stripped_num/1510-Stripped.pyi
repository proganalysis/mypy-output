# (generated with --quick)

from typing import Any, Coroutine, Optional

CACHE_ROOT_DIR: str
CacheBackend: Any
asyncio: module
diskcache: Any
functools: module
lzma: module
os: module
stat: Any

class DiskCache(Any):
    _cache: Any
    def __init__(self) -> None: ...
    def get(self, key, format = ...) -> Coroutine[Any, Any, Optional[bytes]]: ...
    def modified_since(self, key, format = ...) -> coroutine: ...
    def set(self, key, payload, ttl = ..., format = ...) -> None: ...
