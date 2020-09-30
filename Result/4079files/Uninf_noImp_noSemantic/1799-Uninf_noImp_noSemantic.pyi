from tests.server.api.v1.fixtures import http_request as http_request
from typing import Any

class TestBaseHandler:
    def test_write_error(self, handler: Any, mock_exc_info: Any) -> None: ...
    def test_write_error_202(self, handler: Any, mock_exc_info_202: Any) -> None: ...
    def test_log_exception_uncaught(self, mocked_error: Any, handler: Any, mock_exc_info: Any) -> None: ...
    def test_log_exception_http_error(self, mocked_warning: Any, handler: Any, mock_exc_info_http: Any) -> None: ...