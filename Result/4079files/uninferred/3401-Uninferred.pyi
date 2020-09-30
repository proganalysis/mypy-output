from ._resource_op import ResourceOp
from typing import Any, Dict, List

VOLUME_MODE_RWO: Any
VOLUME_MODE_RWM: Any
VOLUME_MODE_ROM: Any

class VolumeOp(ResourceOp):
    attribute_outputs: Any = ...
    volume: Any = ...
    def __init__(self, resource_name: str=..., size: str=..., storage_class: str=..., modes: List[str]=..., annotations: Dict[str, str]=..., data_source: Any=..., **kwargs: Any) -> None: ...
    def _validate_memory_string(self, memory_string: Any) -> None: ...