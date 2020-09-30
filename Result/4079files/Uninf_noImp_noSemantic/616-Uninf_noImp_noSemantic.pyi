from clang.cindex import Cursor, CursorKind, TranslationUnit
from typing import Any

def find_child(parent: Cursor, kind: CursorKind, spelling: str) -> Any: ...
def debug_cursor(node: Cursor) -> Any: ...
def print_all_of_kind(parent: Cursor, kind: CursorKind) -> Any: ...
def get_main(translation_unit: TranslationUnit) -> Cursor: ...
def dump(cursor: Cursor) -> Any: ...
def get_translation_unit(compilation_database_dir: str, cpp_path: str) -> TranslationUnit: ...
def test(args: Any) -> None: ...
