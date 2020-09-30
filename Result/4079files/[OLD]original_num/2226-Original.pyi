# (generated with --quick)

from typing import Any

np: module

class FrameBuffer:
    __doc__: str
    dtype: Any
    frame_buffer: Any
    length: Any
    shape: Any
    def __init__(self, shape, dtype = ...) -> None: ...
    def add_state_to_buffer(self, state) -> None: ...
    def get_buffer(self) -> Any: ...
    def get_buffer_with(self, state) -> Any: ...
    def reset(self) -> None: ...
    def set_buffer(self, frame_buffer) -> None: ...