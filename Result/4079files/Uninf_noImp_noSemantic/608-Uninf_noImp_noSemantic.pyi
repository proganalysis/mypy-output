from . import Operation
from typing import Any

class TranslateOperation(Operation.Operation):
    _node: Any = ...
    _old_transformation: Any = ...
    _translation: Any = ...
    _set_position: Any = ...
    def __init__(self, node: Any, translation: Any, set_position: bool = ...) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...
    def mergeWith(self, other: Any): ...
    def __repr__(self): ...