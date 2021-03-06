from enum import Enum
from microcosm_flask.paging import OffsetLimitPageSchema
from typing import Any, Optional

class TestEnum(Enum):
    A: str = ...
    B: str = ...
    def __str__(self): ...

class SearchAddressPageSchema(OffsetLimitPageSchema):
    list_param: Any = ...
    enum_param: Any = ...

def add_request_id(headers: Any, response_data: Any) -> None: ...

PERSON_MAPPINGS: Any
ADDRESS_MAPPINGS: Any

class TestCRUD:
    graph: Any = ...
    client: Any = ...
    def setup(self) -> None: ...
    def assert_response(self, response: Any, status_code: Any, data: Optional[Any] = ...) -> None: ...
    def test_search(self) -> None: ...
    def test_count(self) -> None: ...
    def test_search_with_context(self) -> None: ...
    def test_reuse_search_self_link(self) -> None: ...
    def test_delete_with_params(self) -> None: ...
    def test_create(self) -> None: ...
    def test_create_empty_object(self) -> None: ...
    def test_create_malformed(self) -> None: ...
    def test_update_batch(self) -> None: ...
    def test_retrieve(self) -> None: ...
    def test_retrieve_qs(self) -> None: ...
    def test_retrieve_not_found(self) -> None: ...
    def test_delete(self) -> None: ...
    def test_delete_not_found(self) -> None: ...
    def test_replace(self) -> None: ...
    def test_update(self) -> None: ...
    def test_update_not_found(self) -> None: ...
