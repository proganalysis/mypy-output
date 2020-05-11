# (generated with --quick)

import io
from typing import Any, Generator, List, Optional, Type, TypeVar
import unittest.case

StringIO: Type[io.StringIO]
Token: Any
unittest: module

_TIntervalSet = TypeVar('_TIntervalSet', bound=IntervalSet)

class IntervalSet(object):
    intervals: Optional[List[range]]
    readOnly: bool
    def __contains__(self, item) -> bool: ...
    def __getitem__(self, item) -> Any: ...
    def __iter__(self) -> Generator[Any, Any, None]: ...
    def __len__(self) -> int: ...
    def addOne(self, v: int) -> None: ...
    def addRange(self, v: range) -> None: ...
    def addSet(self: _TIntervalSet, other: None) -> _TIntervalSet: ...
    def complement(self: _TIntervalSet, start, stop) -> _TIntervalSet: ...
    def elementName(self, literalNames: list, symbolicNames: list, a: int) -> Any: ...
    def reduce(self, k: int) -> None: ...
    def removeOne(self, v) -> None: ...
    def removeRange(self, v) -> None: ...
    def toString(self, literalNames: list, symbolicNames: list) -> str: ...

class TestIntervalSet(unittest.case.TestCase):
    def testComplement(self) -> None: ...
    def testContiguous1(self) -> None: ...
    def testContiguous2(self) -> None: ...
    def testDistinct1(self) -> None: ...
    def testDistinct2(self) -> None: ...
    def testEmpty(self) -> None: ...
    def testOne(self) -> None: ...
    def testOverlapping1(self) -> None: ...
    def testOverlapping2(self) -> None: ...
    def testOverlapping3(self) -> None: ...
    def testRange(self) -> None: ...
    def testTwo(self) -> None: ...
