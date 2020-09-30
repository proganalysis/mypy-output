import hug
from klaxer.users import add_message as add_message
from typing import Any, Optional

CURRENT_FILTERS: Any
RULES: Any

def incoming(service_name: hug.types.text, token: hug.types.text, response: Any, debug: Any=..., body: Any=...) -> Any: ...
def register(response: Any, body: Optional[Any] = ...): ...
def profile(user: hug.directives.user, response: Any, body: Any=...) -> Any: ...
def startup(api: Any) -> None: ...