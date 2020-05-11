# (generated with --quick)

from typing import Any, Callable, Coroutine, Generator, TypeVar

contextlib: module
controller: Any
ctx: Any
eventsequence: Any
exceptions: Any
flow: Any
pprint: module
safecall: Callable[..., contextlib._GeneratorContextManager]
sys: module
traceback: module
types: module
typing: module

_T0 = TypeVar('_T0')

class AddonManager:
    chain: list
    lookup: dict
    master: Any
    def __contains__(self, item) -> bool: ...
    def __init__(self, master) -> None: ...
    def __len__(self) -> int: ...
    def __str__(self) -> str: ...
    def _configure_all(self, options, updated) -> None: ...
    def add(self, *addons) -> None: ...
    def clear(self) -> None: ...
    def get(self, name) -> Any: ...
    def handle_lifecycle(self, name, message) -> Coroutine[Any, Any, None]: ...
    def invoke_addon(self, addon, name, *args, **kwargs) -> None: ...
    def register(self, addon: _T0) -> _T0: ...
    def remove(self, addon) -> None: ...
    def trigger(self, name, *args, **kwargs) -> None: ...

class Loader:
    __doc__: str
    master: Any
    def __init__(self, master) -> None: ...
    def add_command(self, path, func) -> None: ...
    def add_option(self, name, typespec, default, help, choices = ...) -> None: ...

def _get_name(itm) -> Any: ...
def cut_traceback(tb, func_name) -> Any: ...
def traverse(chain) -> Generator[Any, Any, None]: ...
