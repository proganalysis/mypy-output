# (generated with --quick)

import abc
from typing import Any, Callable, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
json: module
logger: logging.Logger
logging: module
requests: module

_FuncT = TypeVar('_FuncT', bound=Callable)

class AbstractDevice(metaclass=abc.ABCMeta):
    __doc__: str
    @abstractmethod
    def close(self) -> Any: ...
    @abstractmethod
    def next(self) -> Any: ...
    @abstractmethod
    def open(self) -> Any: ...

class DummyDevice(AbstractDevice):
    logger: logging.Logger
    def __init__(self, *args, **kwargs) -> None: ...
    def close(self) -> None: ...
    def next(self) -> None: ...
    def open(self) -> None: ...

class OverheadDisplay(AbstractDevice):
    ip_address: Any
    def __init__(self, ip_address, *args, **kwargs) -> None: ...
    def _request(self, method: str) -> Any: ...
    def close(self) -> Any: ...
    def next(self) -> Any: ...
    def open(self) -> Any: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
