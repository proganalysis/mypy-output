from typing import Any, Optional

class Munch(dict):
    def __getattr__(self, k: Any): ...
    def __setattr__(self, k: Any, v: Any) -> None: ...
    def __delattr__(self, k: Any) -> None: ...
    def toDict(self): ...
    def __repr__(self): ...
    def __dir__(self): ...
    __members__: Any = ...
    @classmethod
    def fromDict(cls, d: Any): ...
    def copy(self): ...

class DefaultMunch(Munch):
    __default__: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __getattr__(self, k: Any): ...
    def __setattr__(self, k: Any, v: Any): ...
    def __getitem__(self, k: Any): ...
    @classmethod
    def fromDict(cls, d: Any, default: Optional[Any] = ...): ...
    def copy(self): ...
    def __repr__(self): ...

def munchify(x: Any, factory: Any = ...): ...
def unmunchify(x: Any): ...
