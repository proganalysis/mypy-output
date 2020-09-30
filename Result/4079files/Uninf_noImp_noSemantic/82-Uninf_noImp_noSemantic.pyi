from ..recurrentshop.cells import *
from typing import Any, Optional

class LSTMDecoderCell(ExtendedRNNCell):
    hidden_dim: Any = ...
    def __init__(self, hidden_dim: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def build_model(self, input_shape: Any): ...

class AttentionDecoderCell(ExtendedRNNCell):
    hidden_dim: Any = ...
    input_ndim: int = ...
    def __init__(self, hidden_dim: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def build_model(self, input_shape: Any): ...