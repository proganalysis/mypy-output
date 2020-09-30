# (generated with --quick)

from typing import Any, Callable, TypeVar
import unittest.case

unittest: module

E = TypeVar('E', bound=Exception)
T = TypeVar('T')

class TestResultType(unittest.case.TestCase):
    __doc__: str
    def test_and_then(self) -> None: ...
    def test_conjuct(self) -> None: ...
    def test_context_management(self) -> None: ...
    def test_disjunct(self) -> None: ...
    def test_err_constructor(self) -> None: ...
    def test_is_err(self) -> None: ...
    def test_is_ok(self) -> None: ...
    def test_map(self) -> None: ...
    def test_map_err(self) -> None: ...
    def test_ok_constructor(self) -> None: ...
    def test_or_else(self) -> None: ...
    def test_try_combinator(self) -> None: ...

def Err(error: E) -> Any: ...
def Ok(value: T) -> Any: ...
def try_(fn) -> Callable: ...
