from typing import Any

scraper: Any
VALID_CROSSLINK_TARGETS: Any
INVALID_CROSSLINK_TARGETS: Any
VALID_URI_TARGETS: Any
INVALID_URI_TARGETS: Any

def test_parse_valid_uri_target() -> None: ...
def test_parse_invalid_uri_target() -> None: ...
def test_parse_valid_crosslink_target() -> None: ...
def test_parse_invalid_crosslink_target() -> None: ...
