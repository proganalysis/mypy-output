import unittest
from typing import Any, Optional

TMP_PATH: Any

class TestUnsupervicedModel(unittest.TestCase):
    x: Any = ...
    def setUp(self) -> None: ...
    def train(self, ae: Any, model_params: Optional[Any] = ...): ...
    def test_parametric_tsne(self) -> None: ...
    def test_P(self) -> None: ...
