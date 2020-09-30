# (generated with --quick)

import collections
import flask.wrappers
from typing import Any, Dict, Iterable, Optional, Type

Queue: Any
Response: Type[flask.wrappers.Response]
deque: Type[collections.deque]
gevent: Any
json: module
random: module
request: flask.wrappers.Request
string: module

class Channel(object):
    history: collections.deque
    subscriptions: list
    def __init__(self, history_size: int = ...) -> None: ...
    def _add_history(self, q, last_id: Optional[str]) -> None: ...
    def comment(self, msg: str = ...) -> None: ...
    def event_generator(self, last_id: Optional[str]) -> Iterable[ServerSentEvent]: ...
    def get_last_id(self) -> str: ...
    def notify(self, message: str) -> None: ...
    def publish(self, event: str, message: dict) -> None: ...
    def subscribe(self) -> flask.wrappers.Response: ...

class Comment(object):
    event_id: Any
    msg: str
    def __init__(self, msg: str) -> None: ...
    def encode(self) -> str: ...

class ServerSentEvent(object):
    __doc__: str
    data: str
    desc_map: Dict[Any, str]
    event: str
    event_id: Any
    def __init__(self, data: str, event: str) -> None: ...
    def encode(self) -> str: ...

def generate_id(size: int = ..., chars: str = ...) -> str: ...