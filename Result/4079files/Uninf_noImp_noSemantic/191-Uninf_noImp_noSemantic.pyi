import unittest
from typing import Any

class TestSASTabulate(unittest.TestCase):
    sas: Any = ...
    cars: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_tabulate(self) -> None: ...
    def test_classes(self) -> None: ...
    def test_vars(self) -> None: ...
    def test_stats(self) -> None: ...
    def test_hierarchy(self): ...
    def test_composition_serialization(self) -> None: ...
    def test_procedure(self): ...
    def test_to_dataframe(self) -> None: ...
