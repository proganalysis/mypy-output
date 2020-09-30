from enum import Enum
from typing import Any

def mkdirs_exists_ok(path: Any) -> None: ...

class TxType(Enum):
    PERSISTENT: int = ...
    CLEAR_ON_MANAGER_START: int = ...
    CLEAR_ON_CAR_START: int = ...

class UnknownKeyName(Exception): ...

keys: Any

def fsync_dir(path: Any) -> None: ...

class FileLock:
    _path: Any = ...
    _create: Any = ...
    _fd: Any = ...
    def __init__(self, path: Any, create: Any) -> None: ...
    def acquire(self) -> None: ...
    def release(self) -> None: ...

class DBAccessor:
    _path: Any = ...
    _vals: Any = ...
    def __init__(self, path: Any) -> None: ...
    def keys(self): ...
    def get(self, key: Any): ...
    def _get_lock(self, create: Any): ...
    def _read_values_locked(self): ...
    def _data_path(self): ...
    def _check_entered(self) -> None: ...

class DBReader(DBAccessor):
    _vals: Any = ...
    def __enter__(self): ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...

class DBWriter(DBAccessor):
    _lock: Any = ...
    _prev_umask: Any = ...
    def __init__(self, path: Any) -> None: ...
    def put(self, key: Any, value: Any) -> None: ...
    def delete(self, key: Any) -> None: ...
    _vals: Any = ...
    def __enter__(self): ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...

def read_db(params_path: Any, key: Any): ...
def write_db(params_path: Any, key: Any, value: Any) -> None: ...

class Params:
    db: Any = ...
    def __init__(self, db: str = ...) -> None: ...
    def transaction(self, write: bool = ...): ...
    def _clear_keys_with_type(self, tx_type: Any) -> None: ...
    def manager_start(self) -> None: ...
    def car_start(self) -> None: ...
    def delete(self, key: Any) -> None: ...
    def get(self, key: Any, block: bool = ...): ...
    def put(self, key: Any, dat: Any) -> None: ...
