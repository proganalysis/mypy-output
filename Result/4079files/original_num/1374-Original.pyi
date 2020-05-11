# (generated with --quick)

from typing import Iterable, Iterator, List, Tuple, TypeVar

sys: module

_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')
_T5 = TypeVar('_T5')
_T6 = TypeVar('_T6')

def apriori(index, minsup) -> List[List[int]]: ...
def contains_all_subsets(candidate, candidates) -> bool: ...
@overload
def product(iter1: Iterable, iter2: Iterable, iter3: Iterable, iter4: Iterable, iter5: Iterable, iter6: Iterable, iter7: Iterable, *iterables: Iterable) -> Iterator[tuple]: ...
@overload
def product(iter1: Iterable[_T1]) -> Iterator[Tuple[_T1]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2]) -> Iterator[Tuple[_T1, _T2]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3]) -> Iterator[Tuple[_T1, _T2, _T3]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3], iter4: Iterable[_T4]) -> Iterator[Tuple[_T1, _T2, _T3, _T4]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3], iter4: Iterable[_T4], iter5: Iterable[_T5]) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3], iter4: Iterable[_T4], iter5: Iterable[_T5], iter6: Iterable[_T6]) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5, _T6]]: ...
@overload
def product(*iterables: Iterable, repeat: int = ...) -> Iterator[tuple]: ...
