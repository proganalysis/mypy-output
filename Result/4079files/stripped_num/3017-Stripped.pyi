# (generated with --quick)

from typing import Any, AsyncIterable, AsyncIterator, Coroutine, Dict, Optional, TypeVar

dateutil: module
get_list_element_hint: Any
is_list_type_hint: Any
uritemplate: Any

T = TypeVar('T')
_T0 = TypeVar('_T0')

class BaseObject(dict):
    __doc__: str
    def __getattr__(self, attr) -> Any: ...
    def __init__(self, document) -> None: ...
    @staticmethod
    def _get_key_mappings() -> Dict[nothing, nothing]: ...
    def _normalise_document(self, document: _T0) -> _T0: ...
    def _normalise_key(self, document, key) -> None: ...
    def _set_from_document(self, document) -> None: ...

class BaseResponseObject(BaseObject):
    __doc__: str
    _client: Any
    _default_urls: Dict[nothing, nothing]
    _fetch_params: Any
    _header_links: Any
    _limits: Optional[BaseObject]
    _url: None
    limits: Any
    def __init__(self, client, document = ..., limits = ..., links = ..., fetch_params = ...) -> None: ...
    def _get_related_fetch_params(self) -> None: ...
    def _get_related_object(self, property_name, element_type, **kwargs) -> coroutine: ...
    def _get_related_url(self, property_name, element_type, **kwargs) -> Any: ...
    def fetch_data(self) -> Coroutine[Any, Any, None]: ...

class PaginatedList(AsyncIterator[T]):
    __doc__: str
    _client: Any
    _current_index: Any
    _current_iter: Any
    _current_page_number: int
    _element_type: Any
    _fetch_params: Any
    _header_links: Any
    _item_counter: int
    _last_raw_limits: Any
    _limits: BaseObject
    _max_items: Any
    _pages: list
    limits: Any
    def __aiter__(self: PaginatedList[nothing]) -> Coroutine[Any, Any, PaginatedList[nothing]]: ...
    def __anext__(self: PaginatedList[nothing]) -> coroutine: ...
    def __init__(self: PaginatedList[nothing], client, element_type, initial_document, limits, links, max_items = ..., fetch_params = ...) -> None: ...
    def _get_next_page(self: PaginatedList[nothing]) -> Coroutine[Any, Any, None]: ...
    def _has_more_pages(self: PaginatedList[nothing]) -> bool: ...
    def _increment_page_number(self: PaginatedList[nothing]) -> None: ...
    def _make_element(self: PaginatedList[nothing], document) -> Any: ...
    def get_all(self: PaginatedList[nothing]) -> Coroutine[Any, Any, list]: ...
    def set_max_items(self: PaginatedList[nothing], max_items) -> None: ...

class PaginatedListProxy(AsyncIterable[T]):
    __doc__: str
    _client: Any
    _element_type: Any
    _fetch_params: Any
    _max_items: Any
    _paginator: Optional[PaginatedList[nothing]]
    _url: Any
    def __aiter__(self: PaginatedListProxy[nothing]) -> coroutine: ...
    def __init__(self: PaginatedListProxy[nothing], client, url, element_type, fetch_params) -> None: ...
    def _get_paginator(self: PaginatedListProxy[nothing]) -> coroutine: ...
    def all(self: PaginatedListProxy[nothing]) -> coroutine: ...
    def limit(self: PaginatedListProxy[nothing], max_items) -> PaginatedListProxy[nothing]: ...
