from collections import namedtuple
from enum import Enum
from typing import Any, Tuple

class Subject(Enum):
    Char: int = ...
    Word: int = ...
    Line: int = ...
    Sentence: int = ...
    Paragraph: int = ...
    Function: int = ...
    Class: int = ...
    FullFile: int = ...

class Direction(Enum):
    Forward: int = ...
    Backward: int = ...

Selection = namedtuple('Selection', ['start', 'end'])

class BufferInitializeException(Exception): ...

class Buffer:
    textl: Any = ...
    _pos: int = ...
    _line: int = ...
    _column: int = ...
    selections: Any = ...
    moveselect_method: Any = ...
    def __init__(self, filepath: str=..., text: str=...) -> None: ...
    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, text: str) -> None: ...
    @property
    def pos(self) -> int: ...
    @pos.setter
    def pos(self, newpos: int) -> None: ...
    @property
    def line(self) -> int: ...
    @line.setter
    def line(self, newline: int) -> None: ...
    @property
    def column(self) -> int: ...
    @column.setter
    def column(self, newcolumn: int) -> None: ...
    @property
    def cur_line_length(self) -> int: ...
    @property
    def line_and_column(self) -> Tuple[int, int]: ...
    @line_and_column.setter
    def line_and_column(self, linecolumn: Tuple[int, int]) -> None: ...
    def update_line_col(self) -> None: ...
    def update_pos(self) -> None: ...
    @property
    def num_lines(self) -> int: ...
    def process_subject(self, count: int, subject: Subject, direction: Direction) -> None: ...
    def ms_char(self, direction: Direction) -> None: ...
    def ms_word(self, direction: Direction) -> None: ...
    def ms_line(self, direction: Direction) -> None: ...
    def ms_sentence(self, direction: Direction) -> None: ...
    def ms_paragraph(self, direction: Direction) -> None: ...
    def ms_function(self, direction: Direction) -> None: ...
    def ms_class(self, direction: Direction) -> None: ...
    def ms_fullfile(self, direction: Direction) -> None: ...
    def empty_selections(self) -> None: ...
    def update_column(self) -> int: ...
    def previous_newline_pos(self) -> int: ...

def main() -> None: ...
