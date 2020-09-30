from typing import Any

class TestDecorators:
    args: Any = ...
    kwargs: Any = ...
    def test_ua_parser(self, monkeypatch: Any) -> None: ...
    def test_regex_us_parser(self, monkeypatch: Any, regexes: Any) -> None: ...

class TestCallbackUserAgentParser:
    def test_undefined_name(self) -> None: ...
    def test_explicit_name(self): ...
    def test_returns_on_success(self): ...
    def test_passed_input(self): ...

class TestRegexUserAgentParser:
    def test_undefined_name(self) -> None: ...
    def test_explicit_name(self): ...
    def test_valid(self, regexes: Any, input: Any): ...
    def test_invalid(self, regexes: Any, input: Any) -> None: ...
    def test_positional_captures(self): ...
    def test_named_captures(self): ...
    def test_mixed_captures(self): ...

class TestParserSet:
    def test_valid(self): ...
    def test_cannot_parse(self) -> None: ...
    def test_error_while_parsing(self, caplog: Any) -> None: ...
    def test_optimizing(self) -> None: ...