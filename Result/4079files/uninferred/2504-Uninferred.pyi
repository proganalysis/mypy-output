from typing import Any

def token(): ...
def test_blank_tokens_are_invalid() -> None: ...
def test_expired_tokens(token: Any) -> None: ...
def test_transformation(token: Any) -> None: ...