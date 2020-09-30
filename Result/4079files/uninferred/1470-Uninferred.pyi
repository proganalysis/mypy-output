from typing import Any

class Serial:
    __port: Any = ...
    __baud_rate: Any = ...
    __message_buffer: str = ...
    __serial: Any = ...
    __receive_message_callback: Any = ...
    def __init__(self, port: str, baud_rate: str) -> None: ...
    def add_callback(self, receive_message_callback: Any) -> None: ...
    def connect(self) -> None: ...
    def disconnect(self) -> None: ...
    def send(self, value: str) -> Any: ...
    def loop(self) -> None: ...
    def __has_received_full_message(self): ...