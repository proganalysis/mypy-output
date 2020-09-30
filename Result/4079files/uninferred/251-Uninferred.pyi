import abc
from typing import Any, Optional

KEY_DELIMITER: str

class Driver(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def get(self, key: str) -> Any: ...
    @abc.abstractmethod
    async def set(self, key: str, value: Any) -> Any: ...
    @abc.abstractmethod
    async def delete(self, key: str, value: Any) -> None: ...
    @abc.abstractmethod
    async def expire(self, key: str, time: int) -> Any: ...
    @abc.abstractmethod
    async def lpush(self, key: Any, value: Any) -> Any: ...
    @abc.abstractmethod
    async def rpop(self, key: Any) -> Any: ...

class Redis(Driver):
    __slots__: Any = ...
    url: Any = ...
    db_number: Any = ...
    started: bool = ...
    connection: Any = ...
    startup_lock: Any = ...
    def __init__(self, url: Any, number: int = ...) -> None: ...
    async def ensure_started(self) -> None: ...
    @staticmethod
    def decipher(value: Any): ...
    async def get(self, key: Any): ...
    async def set(self, key: Any, value: Any): ...
    async def delete(self, key: Any): ...
    async def expire(self, key: Any, time: Any): ...
    async def lpush(self, key: Any, value: Any): ...
    async def rpop(self, key: Any): ...
    async def llen(self, key: Any): ...

class Disk(Driver):
    __slots__: Any = ...
    filename: Any = ...
    data: Any = ...
    def __init__(self, filename: str=...): ...
    def load(self) -> None: ...
    def save(self) -> None: ...
    def is_expired(self, key: Any): ...
    @staticmethod
    def decipher(value: Any): ...
    async def get(self, key: Any): ...
    async def set(self, key: Any, value: Any) -> None: ...
    async def delete(self, key: Any) -> None: ...
    async def expire(self, key: Any, seconds: Any) -> None: ...
    async def lpush(self, key: Any, value: Any) -> None: ...
    async def rpop(self, key: Any): ...
    async def llen(self, key: Any): ...

class Interface:
    __slots__: Any = ...
    driver: Any = ...
    def __init__(self, driver: Driver) -> None: ...
    async def get(self, *keys: Any): ...
    async def set(self, *args: Any, expire: Optional[Any] = ...) -> None: ...
    async def get_json(self, *keys: Any): ...
    async def set_json(self, *args: Any, expire: Optional[Any] = ...) -> None: ...
    async def lpush(self, *args: Any) -> None: ...
    async def rpop(self, *keys: Any): ...
    async def delete(self, *args: Any) -> None: ...
    async def expire(self, *args: Any) -> None: ...
    async def llen(self, *keys: Any): ...

def create_redis(url: Any, number: int = ...): ...
def create_disk(filename: Any): ...
def reduce_key(keys: Any): ...
def reduce_key_val(keys: Any): ...
