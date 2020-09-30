import threading
import unittest
from method_proxy import MethodWrapperProxy
from typing import Any, Optional

logger: Any

def command(method: Any): ...

class Actor(threading.Thread):
    _commands: Any = ...
    _must_stop: bool = ...
    exception_handler: Any = ...
    def __init__(self) -> None: ...
    def enqueue(self, method: Any, args: Optional[Any] = ..., kwargs: Optional[Any] = ...) -> None: ...
    def stop(self) -> None: ...
    def run(self) -> None: ...

class ActorTest(unittest.TestCase):
    def raise_hell(self, e: Any) -> None: ...
    nice: bool = ...
    def play_nice(self) -> None: ...
    def produce_exception(self, handler: Optional[Any] = ...) -> None: ...
    def test_actor_continues_running_on_exception_without_handler(self) -> None: ...
    def test_actor_continues_running_on_exception_with_handler(self) -> None: ...

class ActiveObjectProxy(MethodWrapperProxy):
    actor: Any = ...
    def __init__(self, actor: Any, delegate: Any) -> None: ...
    @staticmethod
    def enqueue(proxy: Any, target: Any, name: Any, method: Any): ...

class DoitBackgroundTask:
    called: bool = ...
    def doit(self) -> None: ...
    def test_thread(self, t: Any, test: Any) -> None: ...

class ActiveObjectProxyTest(unittest.TestCase):
    def test_actor_thread_terminates(self) -> None: ...
    def test_proxy_methods_execute(self) -> None: ...
    def test_proxy_methods_execute_on_thread(self) -> None: ...