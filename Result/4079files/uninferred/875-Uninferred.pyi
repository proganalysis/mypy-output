from commands.base import Command
from typing import Any

class Gocode(Command):
    vid: Any = ...
    path: Any = ...
    code: Any = ...
    offset: Any = ...
    add_params: Any = ...
    go_env: Any = ...
    def __init__(self, callback: Any, uid: Any, vid: Any, code: Any, path: Any, offset: Any, param: Any, go_env: Any) -> None: ...
    def run(self) -> None: ...