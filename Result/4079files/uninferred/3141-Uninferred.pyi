from typing import Any, List

def cli(ctx: Any, path: str, lib: str, config: str, env: List[str]) -> Any: ...
def show(ctx: Any, raw: bool, validate_signatures: bool, k: str, ignore_env: bool) -> None: ...
def apply(ctx: Any) -> None: ...
def update(ctx: Any, lock_all: bool) -> None: ...
def main() -> None: ...