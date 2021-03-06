# (generated with --quick)

from typing import Any, NoReturn

basics: Any
importlib: module

class AbstractAggregator(Any, metaclass=AggregatorRegistry):
    def provides(self) -> NoReturn: ...
    def requires(self) -> NoReturn: ...
    def run(self) -> None: ...

class AggregatorRegistry(type):
    aggregators: dict
    def __new__(cls, name, bases, dct) -> Any: ...
    @classmethod
    def get(cls, name) -> Any: ...
    @classmethod
    def load(cls, *aggregator_modules) -> None: ...
