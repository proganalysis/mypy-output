from typing import Any

class AutoNamer:
    __basename: Any = ...
    __last_postfix: int = ...
    def __init__(self, basename: Any) -> None: ...
    def get_next(self, existing_names: Any, prefix: str = ...): ...
    def revert(self) -> None: ...
    def reset(self) -> None: ...

_system_defined_names: Any

def is_valid_name(word: Any): ...
def get_state_attrs(obj: Any): ...
def get_module(module: Any): ...
def get_param_func(param_names: Any): ...
