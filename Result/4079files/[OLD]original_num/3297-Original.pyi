# (generated with --quick)

import concurrent.futures._base
import hashlib
import threading
from typing import Any, Coroutine, List, Type, Union

Container: Any
Event: Type[threading.Event]
FSMBehaviour: Any
Message: Any
PresenceManager: Any
SimpleMessageDispatcher: Any
TraceStore: Any
WebApp: Any
aiosasl: Any
aioxmpp: Any
asyncio: module
ibr: Any
logger: logging.Logger
logging: module
sys: module

class Agent(object):
    _alive: threading.Event
    _values: dict
    avatar: Any
    behaviours: list
    client: Any
    conn_coro: Any
    container: Any
    jid: Any
    loop: Any
    message_dispatcher: Any
    name: Any
    password: Any
    presence: Any
    stream: Any
    traces: Any
    verify_security: Any
    web: Any
    def __init__(self, jid, password, verify_security = ...) -> None: ...
    def _async_connect(self) -> Coroutine[Any, Any, None]: ...
    def _async_register(self) -> Coroutine[Any, Any, None]: ...
    def _async_start(self, auto_register = ...) -> Coroutine[Any, Any, None]: ...
    def _async_stop(self) -> Coroutine[Any, Any, None]: ...
    def _message_received(self, msg) -> list: ...
    def add_behaviour(self, behaviour, template = ...) -> None: ...
    @staticmethod
    def build_avatar_url(jid) -> str: ...
    def dispatch(self, msg) -> List[concurrent.futures._base.Future]: ...
    def get(self, name) -> None: ...
    def has_behaviour(self, behaviour) -> bool: ...
    def is_alive(self) -> bool: ...
    def remove_behaviour(self, behaviour) -> None: ...
    def set(self, name, value) -> None: ...
    def set_container(self, container) -> None: ...
    def set_loop(self, loop) -> None: ...
    def setup(self) -> Coroutine[Any, Any, None]: ...
    def start(self, auto_register = ...) -> Any: ...
    def stop(self) -> Any: ...
    def submit(self, coro) -> concurrent.futures._base.Future: ...

class AuthenticationFailure(Exception):
    __doc__: str

def md5(__string: Union[bytearray, bytes, memoryview] = ...) -> hashlib._Hash: ...
