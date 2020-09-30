import mitmproxy.types
import typing
from typing import Any

class KeyBindingError(Exception): ...

Contexts: Any
navkeys: Any

class Binding:
    help: Any = ...
    def __init__(self, key: Any, command: Any, contexts: Any, help: Any) -> None: ...
    def keyspec(self): ...
    def sortkey(self): ...

class Keymap:
    executor: Any = ...
    keys: Any = ...
    bindings: Any = ...
    def __init__(self, master: Any) -> None: ...
    def _check_contexts(self, contexts: Any) -> None: ...
    def add(self, key: str, command: str, contexts: typing.Sequence[str], help: Any=...) -> None: ...
    def remove(self, key: str, contexts: typing.Sequence[str]) -> None: ...
    def bind(self, binding: Binding) -> None: ...
    def unbind(self, binding: Binding) -> None: ...
    def get(self, context: str, key: str) -> typing.Optional[Binding]: ...
    def list(self, context: str) -> typing.Sequence[Binding]: ...
    def handle(self, context: str, key: str) -> typing.Optional[str]: ...
    def handle_only(self, context: str, key: str) -> typing.Optional[str]: ...

keyAttrs: Any
requiredKeyAttrs: Any

class KeymapConfig:
    defaultFile: str = ...
    def keymap_load_path(self, path: mitmproxy.types.Path) -> None: ...
    def running(self) -> None: ...
    def load_path(self, km: Any, p: Any) -> None: ...
    def parse(self, text: Any): ...
