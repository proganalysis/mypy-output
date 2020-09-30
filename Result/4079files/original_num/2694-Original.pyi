# (generated with --quick)

import numpy
from typing import Any, Iterable, Optional, TypeVar

AffineTransform: Any
AffineTransformable: Any
CoordinateSystem: Any
CoordinateSystemAxes: Any
CoordinateSystemSpace: Any
_ras_mm: Any
np: module
streamlines: module

_TStreamline = TypeVar('_TStreamline', bound=Streamline)
_TStreamlines = TypeVar('_TStreamlines', bound=Streamlines)

class Streamline(object):
    __doc__: str
    _data: Any
    _points: Any
    data: Any
    length: Any
    points: Any
    def __contains__(self, point) -> Any: ...
    def __getitem__(self, key) -> Any: ...
    def __init__(self, points = ..., data = ...) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> reversed: ...
    def distance(left: Streamline, right, nb_points = ...) -> Any: ...
    def reorient(self: _TStreamline, template) -> _TStreamline: ...
    def resample(self, nb_points) -> None: ...
    def reverse(self) -> None: ...
    def smooth(self: _TStreamline, knot_distance = ...) -> _TStreamline: ...

class Streamlines(Any):
    __doc__: str
    _items: Any
    _transformable_points: Iterable[numpy.ndarray]
    lengths: Any
    def __contains__(self, streamline) -> bool: ...
    def __getitem__(self, key) -> Any: ...
    def __iadd__(self: _TStreamlines, other: _TStreamlines) -> _TStreamlines: ...
    def __init__(self, iterable: Optional[Iterable] = ..., coordinate_system = ..., transforms: Optional[Iterable] = ...) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> reversed: ...
    def __str__(self) -> str: ...
    def append(self, streamline) -> None: ...
    def filter(self: _TStreamlines, min_length = ...) -> _TStreamlines: ...
    def reorient(self, template = ...) -> None: ...
    def resample(self, nb_points = ...) -> None: ...
    def reverse(self) -> None: ...
    def smooth(self: _TStreamlines, knot_distance = ...) -> _TStreamlines: ...

def distance(left, right, nb_points = ...) -> Any: ...
def hash(array) -> int: ...
def length(streamline) -> Any: ...
def reorient(streamline, template) -> numpy.ndarray: ...
def resample(streamline, nb_points) -> Any: ...
def smooth(array, knot_distance = ...) -> Any: ...
def transform(array, affine) -> Any: ...
