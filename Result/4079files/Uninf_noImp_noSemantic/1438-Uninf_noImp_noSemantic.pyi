from abc import ABCMeta, abstractmethod
from typing import Any

logger: Any

class FilePushError(Exception):
    def __init__(self, message: Any) -> None: ...

class EngineExecutionError(Exception):
    def __init__(self, message: Any) -> None: ...

class FilePullError(Exception):
    def __init__(self, message: Any) -> None: ...

class AbstractRunner(metaclass=ABCMeta):
    @abstractmethod
    def run(self, container_name: Any, filename: Any, function_name: Any, input_str: Any): ...

class CodeRunner(AbstractRunner):
    util_files: Any = ...
    run_script_filename: str = ...
    def __init__(self, language: Any) -> None: ...
    def run(self, container_name: Any, code_filename: Any, function_name: Any, input_tuples: Any): ...
