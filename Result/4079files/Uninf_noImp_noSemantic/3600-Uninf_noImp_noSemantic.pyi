from .. import AbstractServiceHandler
from typing import Any

class ServiceHandler(AbstractServiceHandler):
    _search_base: str = ...
    def __init__(self) -> None: ...
    def get_all_episodes(self, stream: Any, **kwargs: Any): ...
    def _get_feed_episodes(self, show_key: Any, **kwargs: Any): ...
    def get_stream_link(self, stream: Any) -> None: ...
    def get_stream_info(self, stream: Any, **kwargs: Any) -> None: ...
    def extract_show_key(self, url: Any) -> None: ...
    def get_seasonal_streams(self, **kwargs: Any): ...

def _verify_feed(feed: Any): ...
def _is_valid_episode(feed_episode: Any): ...
def _digest_episode(feed_episode: Any): ...

_exludors: Any
_num_extractors: Any

def _extract_episode_num(name: Any): ...
