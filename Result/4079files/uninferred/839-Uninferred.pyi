import unittest
from typing import Any

log: Any

class TestPointing(unittest.TestCase):
    doplot: bool = ...
    midcore: Any = ...
    nants: Any = ...
    dir: Any = ...
    ntimes: int = ...
    times: Any = ...
    frequency: Any = ...
    channel_bandwidth: Any = ...
    phasecentre: Any = ...
    vis: Any = ...
    model: Any = ...
    def setUp(self) -> None: ...
    def test_simulate_gaintable_from_time_series(self) -> None: ...
