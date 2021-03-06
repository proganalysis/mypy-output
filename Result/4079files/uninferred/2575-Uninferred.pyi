from nbp.bodies import Body
from typing import Any

class BodyState: ...

class BodyState:
    def __init__(self, bodies: [Body], ticks: int, time: float, delta_time: float) -> None: ...
    def to_dict(self) -> dict: ...
    @staticmethod
    def from_dict(dictionary: dict) -> BodyState: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
