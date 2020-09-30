# (generated with --quick)

import asyncio.events
from typing import Any, Callable, IO, List, Optional, TextIO
import unittest.case

asyncio: module
config: Any
config_file: TextIO
json: module
rocket_snake: Any
time: module
unittest: module

class AsyncTester(unittest.case.TestCase):
    __doc__: str
    running_loop: asyncio.events.AbstractEventLoop
    time_track_stack: List[float]
    @staticmethod
    def _do_async_code(coro) -> Any: ...
    def setUp(self, *args, **kwargs) -> None: ...
    def tearDown(self, *args, **kwargs) -> None: ...
    def time_track(self, text = ...) -> Any: ...

class Tester(AsyncTester):
    executed_requests: int
    running_loop: asyncio.events.AbstractEventLoop
    time_track_stack: List[float]
    def do_multiple(self, func, times = ..., text = ...) -> coroutine: ...
    def test_data_endpoints(*args, **kwargs) -> None: ...
    def test_platforms_throughput(*args, **kwargs) -> None: ...
    def test_player_endpoints(*args, **kwargs) -> None: ...
    def test_player_search(*args, **kwargs) -> None: ...
    def test_playlists_throughput(*args, **kwargs) -> None: ...
    def test_seasons_throughput(*args, **kwargs) -> None: ...
    def test_tiers_throughput(*args, **kwargs) -> None: ...

def async_test(f) -> Callable: ...
def pprint(object: object, stream: Optional[IO[str]] = ..., indent: int = ..., width: int = ..., depth: Optional[int] = ..., *, compact: bool = ...) -> None: ...
