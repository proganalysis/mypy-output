from .Point import Point
from typing import Any

class Geometry:
    axle: Any = ...
    points: Any = ...
    size: int = ...
    solved: bool = ...
    def __init__(self, length: int=...) -> None: ...
    def addpoint(self, point: Point, sort: bool=...) -> Any: ...
    def addweight(self, startpoint: Point, endpoint: Point, weight: float=...) -> Any: ...
    def addtorqueload(self, startpoint: Point, endpoint: Point, Torque_per_mm: float=...) -> Any: ...
    def sort(self): ...
    def getA(self): ...
    def getx(self): ...
    def getb(self): ...
