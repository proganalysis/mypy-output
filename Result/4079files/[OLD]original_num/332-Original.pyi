# (generated with --quick)

from typing import Any

MongoConnection: Any
TimeSeriesBase: Any
functools: module

class MongoTickStore(Any): ...

class MongoTimeSeries(Any):
    __doc__: str
    _db: Any
    client: Any
    db: Any
    query: None
    resolution: Any
    server: Any
    def __init__(self, resolution, db = ..., server = ...) -> None: ...
    def _set_index(self) -> None: ...
    def add(self, name, *args, **kwargs) -> None: ...
    def add_many(self, key, data, *args, **kwargs) -> None: ...
    def ensure_index(self) -> None: ...
    def get(self, *args, **kwargs) -> None: ...
    def get_collection(self) -> None: ...
