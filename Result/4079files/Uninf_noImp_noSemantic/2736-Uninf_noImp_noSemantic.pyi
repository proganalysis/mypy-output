from logging import debug as debug
from typing import Any

_r: Any
_config: Any

def init_reddit(config: Any) -> None: ...
def _connect_reddit(): ...
def _ensure_connection(): ...
def submit_text_post(subreddit: Any, title: Any, body: Any): ...
def get_shortlink_from_id(id: Any): ...
