# (generated with --quick)

from typing import Any, TypeVar

d: dict
functions: Any
minilang: Any
np: module
numpy: module
options: dict
s: Any
tensor_markov: Any
txt: str
yaml: module

_T0 = TypeVar('_T0')

class NumericEval:
    d: Any
    minilang: Any
    def __call__(self, s) -> Any: ...
    def __init__(self, d, minilang = ...) -> None: ...
    def eval(self, struct) -> Any: ...
    def eval_commentedseq(self, s) -> Any: ...
    def eval_dict(self, d) -> dict: ...
    def eval_float(self, s: _T0) -> _T0: ...
    def eval_int(self, s: _T0) -> _T0: ...
    def eval_list(self, l) -> list: ...
    def eval_ndarray(self, array_in) -> Any: ...
    def eval_nonetype(self, none) -> None: ...
    def eval_ordereddict(self, s) -> dict: ...
    def eval_scalarfloat(self, s) -> float: ...
    def eval_str(self, s) -> Any: ...