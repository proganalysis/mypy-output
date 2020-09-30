from pathlib import Path
from sensibility.edit import Edit, Substitution
from sensibility.vocabulary import Vind
from typing import Any, Optional

class Suggestion:
    line: int
    column: int
    @staticmethod
    def enclose(filename: Path, fix: Edit) -> Suggestion: ...
    def __str__(self) -> str: ...

class Insert(Suggestion):
    token: Any = ...
    tokens: Any = ...
    insert_after: bool = ...
    pos: Any = ...
    def __init__(self, token: Vind, pos: Any, tokens: Any) -> None: ...
    @property
    def line(self): ...
    @property
    def column(self): ...
    @property
    def insert_before(self): ...
    def __str__(self): ...

class Remove(Suggestion):
    pos: Any = ...
    tokens: Any = ...
    def __init__(self, pos: Any, tokens: Any) -> None: ...
    @property
    def token(self): ...
    @property
    def line(self): ...
    @property
    def column(self): ...
    def __str__(self): ...

class Replace(Suggestion):
    fix: Any = ...
    tokens: Any = ...
    def __init__(self, fix: Substitution, tokens: Any) -> None: ...
    @property
    def pos(self) -> int: ...
    @property
    def token(self): ...
    @property
    def line(self): ...
    @property
    def column(self): ...
    def __str__(self) -> str: ...

def format_fix(filename: Path, fix: Edit) -> None: ...
def get_token_line(pos: Any, tokens: Any): ...
def format_line(tokens: Any, insert_space_before: Optional[Any] = ...): ...
def not_implemented() -> None: ...
