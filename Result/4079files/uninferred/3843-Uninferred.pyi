from hodl.block.constants import sc_base_mem as sc_base_mem
from typing import Any

class SCMemoryError(Exception): ...

class SCMemory:
    scind: Any = ...
    size: Any = ...
    peers: Any = ...
    accepts: Any = ...
    def __init__(self, sc: Any, size: Any) -> None: ...
    def distribute_peers(self) -> None: ...
    def push_memory(self, address: Any, sign: Any, mem_hash: Any) -> None: ...
    def clear_accepts(self) -> None: ...
    def __len__(self): ...
    def __str__(self): ...
    @classmethod
    def from_json(cls, s: Any): ...