# (generated with --quick)

from typing import Any, Generator, Tuple

np: module
sparse: Any
timestamp: Any

class GraphManager:
    __doc__: str
    def __contains__(self, name) -> bool: ...
    def __delattr__(self, name) -> None: ...
    def __delitem__(self, name) -> None: ...
    def __getattr__(self, name) -> Any: ...
    def __getitem__(self, thing) -> Any: ...
    def __init__(self, ds, *, axis) -> None: ...
    def __iter__(self) -> Generator[Any, Any, None]: ...
    def __len__(self) -> int: ...
    def __setattr__(self, name, g) -> None: ...
    def __setitem__(self, name, g) -> None: ...
    def _permute(self, ordering) -> None: ...
    def items(self) -> Generator[Tuple[Any, Any], Any, None]: ...
    def keys(self) -> list: ...
    def last_modified(self, name = ...) -> Any: ...

def _renumber(a, keys, values) -> Any: ...