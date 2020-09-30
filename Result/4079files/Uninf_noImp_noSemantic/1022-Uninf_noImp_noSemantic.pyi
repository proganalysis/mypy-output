from typing import Any

__all__: Any
LOG: Any

class LogManager:
    _PARSER: Any = ...
    _DEFAULT_FMT: str = ...
    @classmethod
    def load_config_file(cls, config_file: Any, debug: str = ...) -> None: ...
    @classmethod
    def _set_debug_mode(cls, debug: bool = ...) -> None: ...
    @classmethod
    def _use_config_file(cls, config_file: Any) -> None: ...
    @classmethod
    def _catch_config_file_exception(cls, config_file: Any) -> None: ...
    @classmethod
    def enable_websocket(cls, socket: Any): ...
    @classmethod
    def add_handler(cls, handler: Any) -> None: ...
    @staticmethod
    def filter_session_disconnected(record: Any): ...

HANDLER_FILTER: Any

class NAppLog:
    def __getattribute__(self, name: Any): ...

NAPP_ID_RE: Any

def _detect_napp_id(): ...
