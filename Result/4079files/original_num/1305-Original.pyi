# (generated with --quick)

from typing import Any, Dict, Optional, TypeVar
import urllib.parse

datetime: module

_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')

def merge_dicts(x, y) -> Any: ...
def qiwi_date(date: datetime.datetime) -> str: ...
def sources_list(sources, params: _T1) -> _T1: ...
def split_float(amount: float) -> Dict[str, str]: ...
def stat_dates(start_date, end_date, params: _T2) -> _T2: ...
def url_params(url) -> dict: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
