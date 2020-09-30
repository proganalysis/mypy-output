import typing as t
from .injector import Injector
from typing import Any

Feature: Any
SyncFeatureProvider: Any
AsyncFeatureProvider: Any
FeatureProvider: Any
SyncProviderMap: Any
AsyncProviderMap: Any
FuncType: Any
F: Any

def mark_provides(func: FeatureProvider, feature: Feature) -> None: ...
def provider(func: FeatureProvider) -> FeatureProvider: ...
def provides(feature: Feature) -> Any: ...

class ModuleMeta(type):
    def __new__(mcls: Any, name: Any, bases: Any, attrs: Any): ...

class Module(metaclass=ModuleMeta):
    @classmethod
    def provider(cls: Any, func: FeatureProvider) -> FeatureProvider: ...
    @classmethod
    def provides(cls: Any, feature: Feature) -> Any: ...
    @classmethod
    def register(cls: Any, func: FeatureProvider, feature: t.Optional[Feature]=...) -> None: ...
    def load(self, injector: Injector) -> Any: ...
    def unload(self, injector: Injector) -> Any: ...
