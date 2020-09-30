from typing import Any

class TestGetDefaultLinterConfigs:
    def test_no_linters_returns_empty_dict(self, mocker: Any) -> None: ...
    def test_with_linters(self, mocker: Any) -> None: ...

class TestFilterConfig:
    def test_filter_by_prefix(self, mocker: Any) -> None: ...
    def test_returned_configparser_getlist(self, expected: Any, mocker: Any, option_content: Any) -> None: ...
    def test_sectionproxy_getlist(self, mocker: Any) -> None: ...
