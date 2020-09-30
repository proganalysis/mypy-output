from datetime import datetime
from typing import Any, Dict, Union

SCHEMA: Any

class FormDecodeError(Exception): ...

def _encode_form(form: Dict[str, str]) -> bytes: ...
def decode_form(form_b64: bytes) -> Dict[str, Union[str, datetime]]: ...
def main() -> None: ...
