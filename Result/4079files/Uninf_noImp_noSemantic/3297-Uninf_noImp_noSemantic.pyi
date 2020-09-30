from typing import Any, Optional

logger: Any

class AuthenticationFailure(Exception): ...

class Agent:
    jid: Any = ...
    password: Any = ...
    verify_security: Any = ...
    behaviours: Any = ...
    _values: Any = ...
    conn_coro: Any = ...
    stream: Any = ...
    client: Any = ...
    message_dispatcher: Any = ...
    presence: Any = ...
    loop: Any = ...
    container: Any = ...
    web: Any = ...
    traces: Any = ...
    _alive: Any = ...
    def __init__(self, jid: Any, password: Any, verify_security: bool = ...) -> None: ...
    def set_loop(self, loop: Any) -> None: ...
    def set_container(self, container: Any) -> None: ...
    def start(self, auto_register: bool = ...): ...
    async def _async_start(self, auto_register: bool = ...) -> None: ...
    async def _async_connect(self) -> None: ...
    async def _async_register(self) -> None: ...
    async def setup(self) -> None: ...
    @property
    def name(self): ...
    @property
    def avatar(self): ...
    @staticmethod
    def build_avatar_url(jid: Any): ...
    def submit(self, coro: Any): ...
    def add_behaviour(self, behaviour: Any, template: Optional[Any] = ...) -> None: ...
    def remove_behaviour(self, behaviour: Any) -> None: ...
    def has_behaviour(self, behaviour: Any): ...
    def stop(self): ...
    async def _async_stop(self) -> None: ...
    def is_alive(self): ...
    def set(self, name: Any, value: Any) -> None: ...
    def get(self, name: Any): ...
    def _message_received(self, msg: Any): ...
    def dispatch(self, msg: Any): ...