# (generated with --quick)

from typing import Any, Dict, List, Optional

Module: Any
re: module

class ThermalModule(Any):
    cdevs: List[nothing]
    name: str
    thermal_root: str
    zones: Dict[int, ThermalZone]
    def __init__(self, target) -> None: ...
    def add_thermal_zone(self, _id) -> None: ...
    def disable_all_zones(self) -> None: ...
    @staticmethod
    def probe(target) -> Optional[bool]: ...

class ThermalZone(object):
    name: str
    path: Any
    target: Any
    trip_points: Dict[int, TripPoint]
    def __init__(self, target, root, _id) -> None: ...
    def add_trip_point(self, _id) -> None: ...
    def get_temperature(self) -> Any: ...
    def is_enabled(self) -> Any: ...
    def set_enabled(self, enabled = ...) -> None: ...

class TripPoint(object):
    _id: Any
    target: Any
    temp_node: str
    type_node: str
    zone: Any
    def __init__(self, zone, _id) -> None: ...
    def get_temperature(self) -> Any: ...
    def get_type(self) -> Any: ...
    def set_temperature(self, temperature) -> None: ...
