from typing import Any

class Transaction:
    obj: Any = ...
    __transaction_state: Any = ...
    def __init__(self, obj: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: Any) -> None: ...

class transactional:
    method: Any = ...
    def __init__(self, method: Any) -> None: ...
    def __get__(self, obj: Any, T: Any): ...
