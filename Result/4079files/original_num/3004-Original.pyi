# (generated with --quick)

from typing import Any, Generator, List, Optional, Union

class Fastread(object):
    filename: Optional[str]
    def __init__(self, filename: Optional[str] = ...) -> None: ...
    def _load(self, sep: Optional[str] = ...) -> Generator[Union[str, List[str]], Any, None]: ...
    def find(self, word: Optional[str] = ...) -> Generator[Union[str, List[str]], Any, None]: ...
    def lines(self, sep: Optional[str] = ...) -> Generator[Union[str, List[str]], Any, None]: ...
    def row(self, number: Optional[int] = ...) -> Any: ...