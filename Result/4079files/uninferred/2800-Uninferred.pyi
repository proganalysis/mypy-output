from Qubit import *
from typing import Any

class ControlFlow:
    ql: Any = ...
    vl: Any = ...
    def __init__(self, q: Any, v: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, a: Any, b: Any, c: Any) -> None: ...