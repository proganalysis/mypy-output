# (generated with --quick)

from typing import Any, Generator, List, Union

class Fastread(object):
    filename: Any
    def __init__(self, filename = ...) -> None: ...
    def _load(self, sep = ...) -> Generator[Union[str, List[str]], Any, None]: ...
    def find(self, word = ...) -> Generator[str, Any, None]: ...
    def lines(self, sep = ...) -> Generator[Union[str, List[str]], Any, None]: ...
    def row(self, number = ...) -> Any: ...
