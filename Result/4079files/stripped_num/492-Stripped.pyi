# (generated with --quick)

from typing import Any

Action: Any
L: logging.Logger
json: module
logging: module
pykka: Any

class AppActor(Any):
    __doc__: str
    _config: Any
    def __init__(self) -> None: ...
    def _refresh_config(self, config_file = ...) -> None: ...
    def on_failure(self, exception_type, exception_value, traceback) -> None: ...
    def on_receive(self, msg) -> Any: ...
    def on_start(self) -> None: ...
    def on_stop(self) -> None: ...

def actor_get_or_create(actor, index = ..., *args, **kwargs) -> Any: ...
