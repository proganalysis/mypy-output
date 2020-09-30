# (generated with --quick)

import flow
import logging
from typing import Any, Dict, FrozenSet, Generator, Optional, Tuple, Type

Flow: Type[flow.Flow]
Logger: Type[logging.Logger]

class Memory:
    inner: Dict[Any, flow.Flow]
    logger: logging.Logger
    def __init__(self) -> None: ...
    def get_minimal_timestamp(self) -> Any: ...
    def insert(self, four_tuple, pkt) -> None: ...
    def items(self) -> Generator[Tuple[Any, flow.Flow], Any, None]: ...
    def update(self, four_tuple, pkt) -> None: ...
    def upsert(self, pkt) -> None: ...

def packet_to_four_tuple(pkt) -> Optional[FrozenSet[Tuple[Any, Any]]]: ...
