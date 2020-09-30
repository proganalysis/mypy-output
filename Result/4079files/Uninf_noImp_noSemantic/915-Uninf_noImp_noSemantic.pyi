import _io
from typing import Any, Iterable

def add_timestamp(entry: str) -> str: ...
def remove_timestamp(entry: str) -> str: ...
def get_timestamp(entry: str) -> str: ...
def write_with_timestamps(file: _io.TextIOWrapper, entries: Iterable[str]) -> None: ...
def read_wo_timestamps(entries: Iterable[str]) -> Iterable[str]: ...
def timetuple(entry: str) -> Any: ...
