from typing import Any
from unittest import TestCase

class BaseTestCase(TestCase):
    loop: Any = ...
    db: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...