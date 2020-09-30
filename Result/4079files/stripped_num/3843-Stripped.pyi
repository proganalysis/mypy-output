# (generated with --quick)

from typing import Any, Dict, List

json: module
log: module
one_peer_mem: Any
sc_base_mem: Any

class SCMemory:
    __doc__: str
    accepts: List[Dict[nothing, Dict[str, Any]]]
    peers: List[nothing]
    scind: Any
    size: Any
    def __init__(self, sc, size) -> None: ...
    def __len__(self) -> Any: ...
    def __str__(self) -> str: ...
    def clear_accepts(self) -> None: ...
    def distribute_peers(self) -> None: ...
    @classmethod
    def from_json(cls, s) -> Any: ...
    def push_memory(self, address, sign, mem_hash) -> None: ...

class SCMemoryError(Exception): ...
