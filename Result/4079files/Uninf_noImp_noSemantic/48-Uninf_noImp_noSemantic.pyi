from typing import Any

def basic_memoize(func: Any): ...
def memoize(func: Any = ..., *, cache: Any = ..., key: str = ...): ...
def cache(func: Any = ..., *, key: str = ...): ...
def freeze_as_received(func: Any): ...
def freeze(*args: Any, **kwargs: Any): ...
def only_args(*args: Any, **kwargs: Any): ...
def nop(*args: Any, **kwargs: Any) -> None: ...

class Singleton(type):
    __instance: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...

class Cached(type):
    __cache: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, *args: Any): ...

def instance_cached(cls: Any = ..., *, cache: Any = ...): ...
def lru_cache(maxsize: int = ...): ...
