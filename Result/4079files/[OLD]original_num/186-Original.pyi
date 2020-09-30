# (generated with --quick)

import collections
import enum
from typing import Any, Callable, Dict, Iterable, Optional, Sized, Tuple, Type, TypeVar, Union

Selection = `namedtuple-Selection-start-end`

Enum: Type[enum.Enum]
blist: Any
os: module
sys: module

_EnumType = TypeVar('_EnumType', bound=Type[enum.Enum])
_Tnamedtuple-Selection-start-end = TypeVar('_Tnamedtuple-Selection-start-end', bound=`namedtuple-Selection-start-end`)

class Buffer:
    __doc__: str
    _column: Any
    _line: Any
    _pos: Any
    column: int
    cur_line_length: int
    line: int
    line_and_column: Tuple[int, int]
    moveselect_method: Dict[Any, Callable[[Direction], None]]
    num_lines: int
    pos: int
    selections: Any
    text: str
    textl: Any
    def __init__(self, filepath: Optional[str] = ..., text: Optional[str] = ...) -> None: ...
    def empty_selections(self) -> None: ...
    def ms_char(self, direction: Direction) -> None: ...
    def ms_class(self, direction: Direction) -> None: ...
    def ms_fullfile(self, direction: Direction) -> None: ...
    def ms_function(self, direction: Direction) -> None: ...
    def ms_line(self, direction: Direction) -> None: ...
    def ms_paragraph(self, direction: Direction) -> None: ...
    def ms_sentence(self, direction: Direction) -> None: ...
    def ms_word(self, direction: Direction) -> None: ...
    def previous_newline_pos(self) -> int: ...
    def process_subject(self, count: int, subject: Subject, direction: Direction) -> None: ...
    def update_column(self) -> int: ...
    def update_line_col(self) -> None: ...
    def update_pos(self) -> None: ...

class BufferInitializeException(Exception): ...

class Direction(enum.Enum):
    Backward: int
    Forward: int

class Subject(enum.Enum):
    Char: int
    Class: int
    FullFile: int
    Function: int
    Line: int
    Paragraph: int
    Sentence: int
    Word: int

class `namedtuple-Selection-start-end`(tuple):
    __slots__ = ["end", "start"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    end: Any
    start: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Selection-start-end`], start, end) -> `_Tnamedtuple-Selection-start-end`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Selection-start-end`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Selection-start-end`: ...
    def _replace(self: `_Tnamedtuple-Selection-start-end`, **kwds) -> `_Tnamedtuple-Selection-start-end`: ...

def main() -> None: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def unique(enumeration: _EnumType) -> _EnumType: ...