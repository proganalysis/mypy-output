# (generated with --quick)

import _importlib_modulespec
from typing import Any, Iterable, List, Optional, Type, Union
import unittest
import unittest.case
import unittest.loader
import unittest.runner

TestCase: Type[unittest.case.TestCase]
_pattern: Any
_plant_trie: Any
regex_pattern: Any

class RegexPattern(unittest.case.TestCase):
    def test_regex_pattern(self) -> None: ...

class TestPattern(unittest.case.TestCase):
    __doc__: str
    def test_a_or_abc(self) -> None: ...
    def test_a_or_abc_or_null(self) -> None: ...
    def test_a_or_b(self) -> None: ...
    def test_ab(self) -> None: ...
    def test_abc_or_dbc(self) -> None: ...
    def test_empty(self) -> None: ...
    def test_null_or_ab(self) -> None: ...
    def test_optional_b(self) -> None: ...
    def test_optional_bc(self) -> None: ...

class TestPlantTrie(unittest.case.TestCase):
    __doc__: str
    def test_a_and_optional_b(self) -> None: ...
    def test_alternatives(self) -> None: ...
    def test_empty(self) -> None: ...
    def test_string(self) -> None: ...

def main(module: Optional[Union[str, _importlib_modulespec.ModuleType]] = ..., defaultTest: Optional[Union[str, Iterable[str]]] = ..., argv: Optional[List[str]] = ..., testRunner: Optional[Union[unittest.runner.TestRunner, Type[unittest.runner.TestRunner]]] = ..., testLoader: unittest.loader.TestLoader = ..., exit: bool = ..., verbosity: int = ..., failfast: bool = ..., catchbreak: bool = ..., buffer: bool = ..., warnings: Optional[str] = ...) -> unittest.TestProgram: ...
