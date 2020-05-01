# (generated with --quick)

import pathlib
import redis.client
import redis.exceptions
from typing import Any, Coroutine, Optional, Type

ConnectionError: Type[redis.exceptions.ConnectionError]
CreateDirectoryException: Any
MissingEnv: Any
Path: Type[pathlib.Path]
Redis: Type[redis.client.Redis]
asyncio: module
datetime: Type[datetime.datetime]
os: module
time: module
timedelta: Type[datetime.timedelta]

def check_running(name) -> Optional[bool]: ...
def get_homedir() -> pathlib.Path: ...
def get_socket_path(name) -> str: ...
def get_storage_path() -> pathlib.Path: ...
def is_running() -> Any: ...
def long_sleep(sleep_in_sec, shutdown_check = ...) -> bool: ...
def long_sleep_async(sleep_in_sec, shutdown_check = ...) -> Coroutine[Any, Any, bool]: ...
def safe_create_dir(to_create) -> None: ...
def set_running(name) -> None: ...
def shutdown_requested() -> int: ...
def unset_running(name) -> None: ...