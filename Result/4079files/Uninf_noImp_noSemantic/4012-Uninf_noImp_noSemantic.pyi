from typing import Any

BINDCODE: str
BINDSYM: str

class Bindings:
    content: Any = ...
    def __init__(self, content: Any) -> None: ...
    def get_all_bindings(self): ...
    def translate_bindings(self) -> None: ...
    def write_bindings_info(self) -> None: ...