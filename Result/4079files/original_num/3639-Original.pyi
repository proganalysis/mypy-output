# (generated with --quick)

import abc
import functools
import pathlib
from typing import Any, Callable, Dict, Optional, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
Path: Type[pathlib.Path]
json: module
math: module
toml: module

_FuncT = TypeVar('_FuncT', bound=Callable)
_T = TypeVar('_T')

class DataFileMixin(metaclass=abc.ABCMeta):
    __doc__: str
    _get_by_ID: Any
    def get_enemy_by_ID(self, ID: int, file: str = ...) -> dict: ...
    def get_entity_by_ID(self, ID: int, file: str = ...) -> dict: ...
    def get_item_by_ID(self, ID: int, file: str = ...) -> dict: ...
    def get_npc_by_ID(self, ID: int, file: str = ...) -> dict: ...

class LevelMixin(metaclass=abc.ABCMeta):
    __doc__: str
    _base_exp: int
    experience: int
    exponent: float
    level: int
    max_level: Any
    next_level: int
    def __init__(self, **kwargs) -> None: ...
    def give_exp(self, amount: int, check_level_up = ..., print_exp = ...) -> Optional[str]: ...
    def level_up(self, print_exp: bool = ...) -> Optional[str]: ...

class ReprMixin(metaclass=abc.ABCMeta):
    __doc__: str
    def __repr__(self) -> str: ...

class SpritesMixin(metaclass=abc.ABCMeta):
    __doc__: str
    @staticmethod
    def _SpritesMixin__load_sprites(type: str, obj: str) -> list: ...
    def load_char_sprites(self, name: str) -> list: ...
    def load_item_sprites(self, ID: int) -> list: ...

def __getattr__(name) -> Any: ...
def abstractmethod(callable: _FuncT) -> _FuncT: ...
def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
def lru_cache(maxsize: Optional[int] = ..., typed: bool = ...) -> Callable[[Callable[..., _T]], functools._lru_cache_wrapper[_T]]: ...
