import unittest
from typing import Any

SAMPLE_PATH: Any
TEST_BUILDING: Any

class LaundryTest(unittest.TestCase):
    laundry_data: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def test_get_status_simple(self) -> None: ...
    def test_get_status_detailed(self) -> None: ...
