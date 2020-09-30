from abc import ABCMeta, abstractmethod
from typing import Any

def cached(method: Any): ...

class Cacheable(metaclass=ABCMeta):
    _allow_caching: bool = ...

class Uncacheable(metaclass=ABCMeta):
    _allow_caching: bool = ...

class Immutable(Cacheable):
    def __setattr__(self, key: Any, value: Any) -> None: ...
    def __delattr__(self, item: Any) -> None: ...

class Mutable(Uncacheable):
    def __setattr__(self, key: Any, value: Any) -> None: ...
    def __delattr__(self, item: Any) -> None: ...

class Jsonizable(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def from_json(cls, string: Any): ...
    @abstractmethod
    def to_json(self): ...

class Serializable(metaclass=ABCMeta):
    @abstractmethod
    def serialize(self): ...

class Hexlifiable(metaclass=ABCMeta):
    @abstractmethod
    def hexlify(self): ...

class HexSerializable(Hexlifiable, Serializable, metaclass=ABCMeta):
    def hexlify(self): ...
