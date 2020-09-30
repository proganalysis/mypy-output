from twisted.internet.protocol import Factory, Protocol
from typing import Any

def close_file(file: Any, d: Any) -> None: ...

READ_CHUNK_SIZE: int

class H2Protocol(Protocol):
    conn: Any = ...
    known_proto: Any = ...
    root: Any = ...
    _flow_control_deferreds: Any = ...
    def __init__(self, root: Any) -> None: ...
    def connectionMade(self) -> None: ...
    def dataReceived(self, data: Any) -> None: ...
    def requestReceived(self, headers: Any, stream_id: Any) -> None: ...
    def dataFrameReceived(self, stream_id: Any) -> None: ...
    def sendFile(self, file_path: Any, stream_id: Any) -> None: ...
    def windowUpdated(self, event: Any) -> None: ...
    def _send_file(self, file: Any, stream_id: Any) -> None: ...
    def wait_for_flow_control(self, stream_id: Any): ...

class H2Factory(Factory):
    root: Any = ...
    def __init__(self, root: Any) -> None: ...
    def buildProtocol(self, addr: Any): ...

root: Any
cert_data: Any
key_data: Any
cert: Any
key: Any
options: Any
endpoint: Any
