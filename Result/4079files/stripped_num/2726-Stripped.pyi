# (generated with --quick)

import axes.handlers.proxy
from typing import Any, Callable, Sequence, Type

AxesProxyHandler: Type[axes.handlers.proxy.AxesProxyHandler]

def axes_dispatch(func) -> Callable: ...
def axes_form_invalid(func) -> Callable: ...
def get_lockout_response(request, credentials = ...) -> Any: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...