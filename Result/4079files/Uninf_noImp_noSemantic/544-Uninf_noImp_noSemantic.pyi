from tick.base.simulation import Simu
from typing import Any, Optional

class SimuPointProcess(Simu):
    _attrinfos: Any = ...
    _pp: Any = ...
    _end_time: Any = ...
    max_jumps: Any = ...
    def __init__(self, end_time: Optional[Any] = ..., max_jumps: Optional[Any] = ..., seed: Optional[Any] = ..., verbose: bool = ...) -> None: ...
    @property
    def end_time(self): ...
    @end_time.setter
    def end_time(self, val: Any) -> None: ...
    @property
    def n_nodes(self): ...
    @property
    def simulation_time(self): ...
    @property
    def n_total_jumps(self): ...
    @property
    def timestamps(self): ...
    @property
    def tracked_intensity(self): ...
    @property
    def intensity_tracked_times(self): ...
    @property
    def intensity_track_step(self): ...
    @property
    def seed(self): ...
    _pp_init_seed: Any = ...
    @seed.setter
    def seed(self, val: Any) -> None: ...
    def _simulate(self) -> None: ...
    def track_intensity(self, intensity_track_step: int = ...) -> None: ...
    def is_intensity_tracked(self): ...
    def reset(self) -> None: ...
    def threshold_negative_intensity(self, allow: bool = ...) -> None: ...
    def set_timestamps(self, timestamps: Any, end_time: Optional[Any] = ...) -> None: ...