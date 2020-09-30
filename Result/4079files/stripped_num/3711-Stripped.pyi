# (generated with --quick)

from typing import Any, Callable, Coroutine, Generator, TypeVar

BadArgument: Any
BotMissingPermissions: Any
CommandError: Any
Context: Any
MissingPermissions: Any
MissingRequiredArgument: Any
MultiConverter: Any
check: Any
commands: Any
discord: Any
guild_only: Any
inspect: module
is_nsfw: Any
is_owner: Any
quoted_word: Any

_T0 = TypeVar('_T0')

class Command(Any):
    __doc__: str
    typing: Any
    def __init__(self, *, typing = ..., **kwargs) -> None: ...
    def _parse_arguments(self, ctx) -> Coroutine[Any, Any, None]: ...
    def do_conversion(self, ctx, converter, argument) -> coroutine: ...
    def invoke(self, ctx) -> Coroutine[Any, Any, None]: ...
    def transform(self, ctx, param) -> coroutine: ...

class Group(GroupMixin, Any, Command): ...

class GroupMixin(Any):
    def command(self, *args, **kwargs) -> Callable[[Any], Any]: ...
    def group(self, *args, **kwargs) -> Callable[[Any], Any]: ...

class RecalledArgument:
    __doc__: str
    argument: Any
    def __init__(self, argument) -> None: ...

def _get_words(view) -> Generator[Any, Any, None]: ...
def _has_permissions(ctx, target, **perms) -> bool: ...
def bot_has_permissions(**perms) -> Any: ...
def command(name = ..., cls = ..., **attrs) -> Any: ...
def group(name = ..., invoke_without_command = ..., **attrs) -> Any: ...
def has_permissions(**perms) -> Any: ...
def schedule(interval, wait_until_ready = ..., run_once = ...) -> Callable[[Any], Any]: ...
def user_has_permissions(**perms) -> Any: ...
def when_ready(func: _T0) -> _T0: ...
