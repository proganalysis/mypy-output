# (generated with --quick)

import asyncio.events
import hashlib
from typing import Any, Callable, Coroutine, Dict, Sequence, Union

import_class: Any
settings: Any

class BaseAnalytics(object):
    __doc__: str
    _instances: Dict[tuple, BaseAnalytics]
    def async_init(self) -> Coroutine[Any, Any, None]: ...
    def hash_user_id(self, user_id: str) -> str: ...
    @classmethod
    def instance(cls, *args) -> Coroutine[Any, Any, BaseAnalytics]: ...
    def page_view(self, url: str, title: str, user_id: str, user_lang: str = ...) -> Coroutine[Any, Any, None]: ...

def get_event_loop() -> asyncio.events.AbstractEventLoop: ...
def new_task(func) -> Callable: ...
def providers() -> asyncgenerator: ...
def sha256(__string: Union[bytearray, bytes, memoryview] = ...) -> hashlib._Hash: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...