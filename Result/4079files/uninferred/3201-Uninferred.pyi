from typing import Any, Optional

def run(cmd: Any, *, interact: bool = ..., **kwargs: Any): ...
def run_interactive(cmd: Any): ...
def run_static(cmd: Any, input_data: Optional[Any] = ..., timeout: Optional[Any] = ...): ...
def copy_env(): ...