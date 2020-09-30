from typing import Any, Optional

class TransactionManagementError(Exception): ...

def enter_transaction_management(using: Optional[Any] = ...) -> None: ...
def leave_transaction_management(using: Optional[Any] = ...) -> None: ...
def is_dirty(using: Optional[Any] = ...): ...
def is_managed(using: Optional[Any] = ...): ...
def commit(using: Optional[Any] = ...) -> None: ...
def rollback(using: Optional[Any] = ...) -> None: ...

class Transaction:
    entering: Any = ...
    exiting: Any = ...
    using: Any = ...
    def __init__(self, entering: Any, exiting: Any, using: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    def __call__(self, func: Any): ...

def _transaction_func(entering: Any, exiting: Any, using: Any): ...
def commit_on_success(using: Optional[Any] = ...): ...
def commit_manually(using: Optional[Any] = ...): ...
