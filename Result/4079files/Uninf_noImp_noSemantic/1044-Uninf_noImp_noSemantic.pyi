from Firefly.components.zwave.zwave_device import ZwaveDevice
from Firefly.helpers.device_types.contact_sensor import ContactSensor
from openzwave.network import ZWaveNode
from openzwave.value import ZWaveValue
from typing import Any

ALARM: str
BATTERY: str
CAPABILITIES: Any
COMMANDS: Any
REQUESTS: Any

class ZwaveContactSensor(ContactSensor, ZwaveDevice):
    value_map: Any = ...
    refreshed: bool = ...
    def __init__(self, firefly: Any, package: Any, title: str = ..., initial_values: Any = ..., value_map: Any = ..., **kwargs: Any) -> None: ...
    def export(self, current_values: bool=..., api_view: bool=..., **kwargs: Any) -> Any: ...
    _node: Any = ...
    def update_from_zwave(self, node: ZWaveNode=..., ignore_update: Any=..., values: ZWaveValue=..., values_only: Any=..., **kwargs: Any) -> Any: ...
