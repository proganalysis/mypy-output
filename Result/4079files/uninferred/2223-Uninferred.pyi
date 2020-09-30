from .trait_object import TraitObject
from typing import Any

class UnidentifiedObject(TraitObject):
    @classmethod
    def hook_into(cls, inspector: Any) -> None: ...
    def __str__(self): ...
    def __bool__(self): ...