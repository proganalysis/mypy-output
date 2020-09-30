from typing import Any, Optional

class AbstractCast:
    def __call__(self, value: Any) -> None: ...

class Boolean(AbstractCast):
    default_values: Any = ...
    values: Any = ...
    def __init__(self, values: Optional[Any] = ...) -> None: ...
    def __call__(self, value: Any): ...

class List(AbstractCast):
    delimiter: Any = ...
    quotes: Any = ...
    def __init__(self, delimiter: str = ..., quotes: str = ...) -> None: ...
    def _parse(self, string: Any): ...
    def cast(self, sequence: Any): ...
    def __call__(self, value: Any): ...

class Tuple(List):
    def cast(self, sequence: Any): ...

class Option(AbstractCast):
    options: Any = ...
    def __init__(self, options: Any) -> None: ...
    def __call__(self, value: Any): ...
