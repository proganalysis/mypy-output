from collections.abc import MutableMapping
from typing import Any

_file: str

class Config(MutableMapping):
    _values: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def populate(self, values: Any) -> None: ...
    def to_dict(self): ...
    def __str__(self): ...
    def __repr__(self): ...

config: Any