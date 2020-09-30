import queue
import subprocess
from ...store import PluginStore
from ...utils import State
from typing import Any

class _ListenerInterface:
    _state: Any = ...
    _store: Any = ...
    _queue_tts: Any = ...
    def __init__(self, state: State, store: PluginStore, tts: queue.Queue) -> None: ...
    def __repr__(self): ...
    def _process_result(self, plugin_name: str, process: subprocess.Popen) -> Any: ...
    def listen(self) -> None: ...
    def stop(self) -> None: ...
