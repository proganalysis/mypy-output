# (generated with --quick)

import numbers
import typing
from typing import Any, Optional, Type

Callable: Any
Dict: Any
Generator: Any
Generic: Any
Iterable: Any
Iterator: Any
List: Any
Mapping: Any
Real: Type[numbers.Real]
Sequence: Any
T_1_py3: Any
Tuple: Any
`TypeVar`: Any
Union: Any
abc: module
override: Any

_FuncT = TypeVar('_FuncT', bound=Callable)
_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')
_Ttest_iter = TypeVar('_Ttest_iter', bound=test_iter)

class Custom_Generic(Any):
    val: Any
    def __init__(self, val) -> None: ...
    def v(self) -> Any: ...

class testClass(str):
    def testmeth(self, a, b) -> str: ...
    def testmeth2(self, a: int, b: numbers.Real) -> str: ...
    @classmethod
    def testmeth_class(cls, a: int, b: numbers.Real) -> str: ...
    @classmethod
    def testmeth_class2(cls, a, b) -> str: ...
    @classmethod
    def testmeth_class2_err(cls, a, b) -> str: ...
    @classmethod
    def testmeth_class_raw(cls, a, b) -> str: ...
    def testmeth_forward(self, a, b) -> int: ...
    @staticmethod
    def testmeth_static(a: int, b: numbers.Real) -> str: ...
    @staticmethod
    def testmeth_static2(a, b) -> str: ...
    @staticmethod
    def testmeth_static_raw(a, b) -> str: ...

class testClass2(testClass2Base):
    testmeth: Any
    testmeth2: Any
    testmeth2b: Any
    testmeth3: Any
    testmeth3_err: Any
    testmeth4: Any
    testmeth5: Any
    testmeth6: Any
    def testmeth0(self, a: int, b: numbers.Real) -> str: ...
    def testmeth_err(self, a, b) -> str: ...

class testClass2Base(str):
    def testmeth(self, a, b) -> None: ...
    def testmeth2(self, a, b) -> None: ...
    def testmeth2b(self, a, b) -> None: ...
    def testmeth3(self, a, b) -> None: ...
    def testmeth3_err(self, a, b) -> None: ...
    def testmeth4(self, a, b) -> None: ...
    def testmeth5(self, a, b) -> None: ...

class testClass3(testClass3Base):
    testmeth: Any

class testClass3Base(metaclass=abc.ABCMeta):
    __metaclass__: Type[abc.ABCMeta]
    @abstractmethod
    def testmeth(self, a, b) -> Any: ...

class test_iter:
    itrbl: Any
    pos: int
    def __init__(self, itrbl) -> None: ...
    def __iter__(self: _Ttest_iter) -> _Ttest_iter: ...
    def __next__(self) -> Any: ...
    def next(self) -> Any: ...

class test_iterable:
    tpl: Any
    def __init__(self, tpl) -> None: ...
    def __iter__(self) -> test_iter: ...

class test_iterable_annotated:
    tpl: Any
    def __init__(self, tpl) -> None: ...
    def __iter__(self) -> test_iter: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
def pclb(s, i) -> str: ...
def pclb2(s, i) -> str: ...
def pclb3(s, i) -> str: ...
def testClass2_defTimeCheck() -> None: ...
def testClass2_defTimeCheck2() -> None: ...
def testClass2_defTimeCheck3() -> None: ...
def testClass2_defTimeCheck4() -> None: ...
def testClass3_defTimeCheck() -> None: ...
def testfunc(a: int, b: numbers.Real, c: str) -> Any: ...
def testfunc2(a, b, c) -> typing.Tuple[Any, Any]: ...
def testfunc_Callable_arg(a, b) -> Any: ...
def testfunc_Callable_call_err(a, b) -> Any: ...
def testfunc_Callable_ret(a, b) -> typing.Callable[[Any, Any], Any]: ...
def testfunc_Callable_ret_err() -> int: ...
def testfunc_Dict_arg(a, b) -> None: ...
def testfunc_Dict_ret(a: _T0) -> typing.Dict[Any, typing.Union[int, _T0]]: ...
def testfunc_Dict_ret_err(a: _T0) -> typing.Dict[Any, typing.Union[str, _T0]]: ...
def testfunc_Generator() -> typing.Generator[Optional[typing.Union[int, str]], Any, Optional[typing.Union[float, str]]]: ...
def testfunc_Generator_arg(gen) -> list: ...
def testfunc_Generator_ret() -> typing.Generator[Optional[typing.Union[int, str]], Any, Optional[typing.Union[float, str]]]: ...
def testfunc_Generic_arg(x) -> Any: ...
def testfunc_Generic_ret(x) -> Custom_Generic: ...
def testfunc_Generic_ret_err(x) -> Custom_Generic: ...
def testfunc_Iter_arg(a, b) -> list: ...
def testfunc_Iter_ret() -> typing.List[int]: ...
def testfunc_Iter_ret_err() -> typing.List[int]: ...
def testfunc_Iter_str_arg(a) -> typing.List[int]: ...
def testfunc_Mapping_arg(a, b) -> None: ...
def testfunc_None_arg(a, b) -> Any: ...
def testfunc_None_ret(a, b) -> None: ...
def testfunc_None_ret_err(a: int, b: numbers.Real) -> None: ...
def testfunc_Seq_arg(a) -> int: ...
def testfunc_Seq_ret_List(a: _T0, b: _T1) -> typing.List[typing.Union[_T0, _T1]]: ...
def testfunc_Seq_ret_Tuple(a: _T0, b: _T1) -> typing.Tuple[_T0, _T1]: ...
def testfunc_Seq_ret_err(a: _T0, b: _T1) -> typing.Dict[typing.Union[_T0, _T1], str]: ...
def testfunc_err(a: int, b: numbers.Real, c: str) -> Any: ...
