from typing import Any, Optional

class SpeechSegmentGenerator:
    feature_extraction: Any = ...
    per_label: Any = ...
    per_fold: Any = ...
    per_epoch: Any = ...
    duration: Any = ...
    parallel: Any = ...
    label_min_duration: Any = ...
    in_memory: Any = ...
    min_duration: Any = ...
    max_duration: Any = ...
    min_duration_: Any = ...
    weighted_: bool = ...
    def __init__(self, feature_extraction: Any, protocol: Any, subset: str = ..., per_label: int = ..., per_fold: Optional[Any] = ..., per_epoch: int = ..., duration: Optional[Any] = ..., min_duration: Optional[Any] = ..., max_duration: Optional[Any] = ..., label_min_duration: float = ..., parallel: int = ..., in_memory: bool = ...) -> None: ...
    data_: Any = ...
    file_labels_: Any = ...
    segment_labels_: Any = ...
    def _load_metadata(self, protocol: Any, subset: str = ...) -> None: ...
    def generator(self) -> None: ...
    @property
    def batch_size(self): ...
    @property
    def batches_per_epoch(self): ...
    @property
    def signature(self): ...
    @property
    def specifications(self): ...
    def __call__(self) -> None: ...
