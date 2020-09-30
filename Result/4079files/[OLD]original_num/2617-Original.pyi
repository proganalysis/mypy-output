# (generated with --quick)

from typing import Any, Callable, Dict, Generator, Iterable, List, MutableSequence, Sized, Tuple, Type, TypeVar

ListOfWords = List[List[ElianCharacter]]

CHARACTERS: Dict[str, ElianCharacter]
SPACE: ElianCharacter
argparse: module
collections: module
typing: module

_TElianCharacter = TypeVar('_TElianCharacter', bound=ElianCharacter)

class ElianCharacter(tuple):
    __slots__ = ["lower", "middle", "upper"]
    __dict__: collections.OrderedDict[str, str]
    _field_defaults: collections.OrderedDict[str, str]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[str, str, str]
    lower: str
    middle: str
    upper: str
    def __getnewargs__(self) -> Tuple[str, str, str]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TElianCharacter], upper: str, middle: str, lower: str) -> _TElianCharacter: ...
    def _asdict(self) -> collections.OrderedDict[str, str]: ...
    @classmethod
    def _make(cls: Type[_TElianCharacter], iterable: Iterable[str], new = ..., len: Callable[[Sized], int] = ...) -> _TElianCharacter: ...
    def _replace(self: _TElianCharacter, **kwds: str) -> _TElianCharacter: ...

class ElianScript(MutableSequence):
    _characters: List[ElianCharacter]
    def __delitem__(self, ii: int) -> None: ...
    def __getitem__(self, ii: int) -> Any: ...
    def __init__(self, text: str = ...) -> None: ...
    def __len__(self) -> int: ...
    def __setitem__(self, ii: int, val: ElianCharacter) -> None: ...
    def _chunk_lines(self, space_between_chars: int, space_between_words: int, line_char_limit: int = ...) -> Generator[List[List[ElianCharacter]], Any, None]: ...
    def _chunk_words(self) -> Generator[List[ElianCharacter], Any, None]: ...
    def _line_to_upper_middle_lower(self, line: List[List[ElianCharacter]], word_space_divider: str, char_space_divider: str) -> Tuple[str, str, str]: ...
    def _str_to_elian_chars(self, text: str) -> Generator[ElianCharacter, Any, None]: ...
    def _word_to_upper_middle_lower(self, word: str, char_space_divider: str) -> Tuple[Any, str, Any]: ...
    def extend_str(self, val: str) -> None: ...
    def insert(self, ii: int, val: ElianCharacter) -> None: ...

def cli() -> argparse.Namespace: ...
def main() -> None: ...
