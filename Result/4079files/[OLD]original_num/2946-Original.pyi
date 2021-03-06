# (generated with --quick)

from typing import Any

StoreKeyNotFound: Any

class InMemoryStore:
    __doc__: str
    _data: dict
    def __init__(self) -> None: ...
    def delete(self, key) -> None: ...
    def exists(self, key) -> bool: ...
    def get(self, key) -> Any: ...
    def set(self, key, data) -> None: ...
