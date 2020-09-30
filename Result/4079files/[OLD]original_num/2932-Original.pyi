# (generated with --quick)

import collections
import difflib
import itertools
from typing import Any, Coroutine, List, Optional, Type, Union

PyQuery: Any
SequenceMatcher: Type[difflib.SequenceMatcher]
chain: Type[itertools.chain]
deque: Type[collections.deque]

def __get_closest(query: str, anime_list: List[dict], names) -> dict: ...
def get_anime_url(session_manager, query, names: list) -> Coroutine[Any, Any, Optional[str]]: ...
def get_anime_url_by_id(anime_id) -> str: ...
def get_manga_url(session_manager, query, names: list, author_name = ...) -> Coroutine[Any, Any, Optional[str]]: ...
def get_manga_url_by_id(manga_id) -> str: ...
@overload
def quote(string: bytes, safe: Union[bytes, str] = ...) -> str: ...
@overload
def quote(string: str, safe: Union[bytes, str] = ..., encoding: str = ..., errors: str = ...) -> str: ...
def sanitize_search_text(text: str) -> str: ...