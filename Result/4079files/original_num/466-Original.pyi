# (generated with --quick)

import __future__
from typing import Any, List, NoReturn, Set

EXCEPTIONS: Set[str]
EXTENSION: int
EXTLANG: int
REGION: int
SCRIPT: int
SUBTAG_TYPES: List[str]
VARIANT: int
print_function: __future__._Feature
unicode_literals: __future__._Feature

class LanguageTagError(ValueError): ...

def normalize_characters(tag) -> Any: ...
def order_error(subtag, got, expected) -> NoReturn: ...
def parse_extension(subtags) -> list: ...
def parse_extlang(subtags) -> list: ...
def parse_subtags(subtags, expect = ...) -> list: ...
def parse_tag(tag) -> list: ...
def subtag_error(subtag, expected = ...) -> NoReturn: ...
