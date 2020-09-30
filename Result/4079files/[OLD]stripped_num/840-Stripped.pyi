# (generated with --quick)

import _importlib_modulespec
import contextlib
import doctest
import textwrap
from typing import Any, Callable, Dict, Iterable, Iterator, List, NoReturn, Optional, Type, TypeVar

ELLIPSIS: int
TextWrapper: Type[textwrap.TextWrapper]
VERSION: str
_COLUMNS: int
_DEBUG_PREFIX: str
_ERROR_PREFIX: str
_WARNING_PREFIX: str
__all__: List[str]
_debug: Any
_debug_wrapper: EnhancedTextWrapper
_error_wrapper: EnhancedTextWrapper
_no_prefix_wrapper: EnhancedTextWrapper
_verbose: Any
_verbose_prefix: Any
_verbose_wrapper: Optional[EnhancedTextWrapper]
_warning_wrapper: EnhancedTextWrapper
itertools: module
os: module
sys: module
working_directory: Callable[..., contextlib._GeneratorContextManager]

_T = TypeVar('_T')

class EnhancedTextWrapper(textwrap.TextWrapper):
    __doc__: str
    def __init__(self, width = ..., subsequent_indent = ...) -> None: ...
    def fill(self, msg) -> str: ...

def all_pred(func, iterable) -> bool: ...
def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
def debug(msg) -> None: ...
def debug_is_enabled() -> bool: ...
def die(msg) -> NoReturn: ...
def dropwhile(predicate: Callable[[_T], object], iterable: Iterable[_T]) -> Iterator[_T]: ...
def error(msg) -> None: ...
def info(msg) -> None: ...
def set_debug(debug) -> None: ...
def set_verbosity(verbose, verbose_prefix = ...) -> None: ...
def squeeze_blank_lines(s) -> Any: ...
def strip_margin(s, margin_char = ...) -> str: ...
def testmod(m: Optional[_importlib_modulespec.ModuleType] = ..., name: Optional[str] = ..., globs: Dict[str, Any] = ..., verbose: bool = ..., report: bool = ..., optionflags: int = ..., extraglobs: Dict[str, Any] = ..., raise_on_error: bool = ..., exclude_empty: bool = ...) -> doctest.TestResults: ...
def verbose(msg) -> None: ...
def verbosity_is_enabled() -> Any: ...
def warn(msg) -> None: ...
def wrap2stdout(msg) -> None: ...