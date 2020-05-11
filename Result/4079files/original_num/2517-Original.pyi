# (generated with --quick)

from typing import Any, List, Match, Pattern, Tuple, TypeVar, Union

_ROMAIN_REGEXP: Pattern[str]
_SIMPLIFIED_RE: Pattern[str]
_VOY_COMMUNES: Pattern[str]
_VOY_REPLACE: List[Tuple[Pattern[str], str]]
_Y_SHORT_REPLACE: Pattern[str]
abrev: List[str]
consonnes: str
re: module
unidecode: Any
voyelles: str

_T0 = TypeVar('_T0')

def allonge(f: _T0) -> Union[str, _T0]: ...
def atone(string, caps = ...) -> Any: ...
def clean_double_diacritic(string) -> Any: ...
def communes(g) -> Any: ...
def deramise(r) -> Any: ...
def estRomain(f) -> Match[str]: ...
def listeI(l) -> List[int]: ...
def simplified(string) -> str: ...
