# (generated with --quick)

import argparse
from typing import Any, List, TypeVar

datetime: module
notify2: Any
os: module
sys: module

AnyStr = TypeVar('AnyStr', str, bytes)

def get_args() -> argparse.Namespace: ...
def get_filename(grades_path) -> str: ...
def get_last_grades(grades_path) -> str: ...
def get_timestamp() -> str: ...
def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
def main() -> None: ...
def show_notification(title, description) -> None: ...
def time() -> float: ...
def write_grades(grades, grades_path) -> str: ...