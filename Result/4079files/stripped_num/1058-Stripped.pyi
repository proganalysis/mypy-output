# (generated with --quick)

from typing import Any, Callable, List, Type
import utils

CheckMsg: Type[utils.CheckMsg]
asyncio: module
commands: Any
where: List[Callable]
who: List[Callable[[Any], Any]]

def arg_check(pred, message = ...) -> Callable[[Any], Any]: ...
def has_tag(tag) -> Any: ...
def is_channel(name) -> Any: ...
def is_moderator() -> Any: ...
def is_owner() -> Any: ...
def is_server_owner() -> Any: ...
def is_testing() -> Any: ...
def is_trusted() -> Any: ...
def moderator(ctx) -> Any: ...
def notprivate(ctx) -> bool: ...
def owner(ctx) -> Any: ...
def profiles() -> Any: ...
def server_owner(ctx) -> Any: ...
def tagged(ctx, tag) -> bool: ...
def testing(ctx) -> bool: ...
def tools() -> Any: ...
def trusted(ctx) -> Any: ...
