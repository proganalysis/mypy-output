# (generated with --quick)

from typing import Any, Dict, Generator, SupportsFloat, Tuple

Parameter: Any
Parameters: Any
copy: module
csv: module
np: module
pathlib: module
pd: Any
typing: module
yaml: module

class ParameterGroup(dict):
    _label: Any
    _parameters: dict
    _root: Any
    label: Any
    def __init__(self, label = ...) -> None: ...
    def add_group(self, group) -> None: ...
    def add_parameter(self, parameter) -> None: ...
    def all(self, root = ..., seperator = ...) -> Generator[Tuple[Any, Any], Any, None]: ...
    def as_parameter_dict(self) -> Any: ...
    @classmethod
    def from_csv(cls, filepath, delimiter = ...) -> Any: ...
    @classmethod
    def from_dict(cls, parameter, label = ...) -> Any: ...
    @classmethod
    def from_file(cls, filepath, fmt = ...) -> Any: ...
    @classmethod
    def from_list(cls, parameter, label = ...) -> Any: ...
    @classmethod
    def from_parameter_dict(cls, parameter) -> Any: ...
    @classmethod
    def from_yaml(cls, yaml_string) -> Any: ...
    @classmethod
    def from_yaml_file(cls, filepath) -> Any: ...
    def get(self, label) -> Any: ...
    def get_nr_roots(self) -> int: ...
    def groups(self) -> Generator[Any, Any, None]: ...
    def has(self, label) -> bool: ...
    @classmethod
    def known_formats(cls) -> Dict[str, Any]: ...
    def markdown(self) -> str: ...
    def set_root(self, root) -> None: ...
    def to_csv(self, filename, delimiter = ...) -> None: ...

class ParameterNotFoundException(Exception):
    __doc__: str
    def __init__(self, path, label) -> None: ...

def log(x: SupportsFloat, base: SupportsFloat = ...) -> float: ...