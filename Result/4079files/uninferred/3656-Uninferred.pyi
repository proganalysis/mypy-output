from typing import Any, Optional

class GlobalStandardization:
    def get_context_duration(self): ...
    def __call__(self, features: Any, sliding_window: Optional[Any] = ...): ...

class ShortTermStandardization:
    duration: Any = ...
    def __init__(self, duration: float = ...) -> None: ...
    def get_context_duration(self): ...
    def __call__(self, features: Any, sliding_window: Optional[Any] = ...): ...
