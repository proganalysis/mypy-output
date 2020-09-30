from .content import Content
from .methods import Method
from enum import Enum
from io import BytesIO
from typing import Any, Iterable, Tuple

__all__: Any

class FrameType(Enum):
    METHOD: int = ...
    CONTENT_HEADER: int = ...
    CONTENT_BODY: int = ...
    HEARTBEAT: int = ...

_Frame: Any

class IncompleteData(Exception): ...

def parse_protocol_header(stream: BytesIO) -> Tuple[int, int, int]: ...
def parse_frames(stream: BytesIO) -> Iterable[_Frame]: ...
def dump_protocol_header(major: int, minor: int, revision: int) -> bytes: ...
def dump_frame_method(channel_id: int, method: Method) -> bytes: ...
def dump_frame_content(channel_id: int, content: Content, max_frame_size: int) -> bytes: ...
def dump_frame_heartbeat(channel_id: int) -> bytes: ...
def load(fmt: str, stream: BytesIO, _unpack: Any=...) -> Any: ...
def dump(fmt: str, *values: Any, _pack: Any=...) -> bytes: ...
def _read(stream: BytesIO, length: int) -> Any: ...
def _parse_frame(stream: BytesIO, _unpack: Any=...) -> Any: ...
def _load_item(stream: BytesIO, _unpack: Any=...) -> Any: ...
def _dump_frame(frame_type: FrameType, channel_id: int, data: bytes) -> bytes: ...
def _dump_item(value: Any, _pack: Any=...) -> bytes: ...