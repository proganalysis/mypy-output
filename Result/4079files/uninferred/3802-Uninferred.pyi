from typing import Any

class NAM:
    time_step: int = ...
    dx: int = ...
    folder: Any = ...
    data_files: Any = ...
    dates: Any = ...
    dataset_start: Any = ...
    dataset_end: Any = ...
    def __init__(self, folder: Any) -> None: ...
    @staticmethod
    def filename_to_datetime(filename: Any): ...
    def scan_folder(self) -> None: ...
    def check_complete(self) -> None: ...

class NAM_forecast:
    time_step: int = ...
    dx: int = ...
    folder: Any = ...
    data_files: Any = ...
    dates: Any = ...
    dataset_start: Any = ...
    dataset_end: Any = ...
    def __init__(self, folder: Any) -> None: ...
    def scan_folder(self) -> None: ...
    @staticmethod
    def filename_to_datetime(filename: Any): ...

def main(path_to_dataset: Any, forecast: Any) -> None: ...