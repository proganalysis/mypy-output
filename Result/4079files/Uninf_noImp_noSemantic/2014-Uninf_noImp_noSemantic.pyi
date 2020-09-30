from typing import Any

class ExcelIOException(Exception): ...

class ExcelQtConverter:
    file_name: Any = ...
    px_workbook: Any = ...
    def __init__(self, file_name: Any) -> None: ...
    def to_model(self, name: Any, model_type: Any = ..., header: bool = ...): ...
    def from_model(self, qt_model: Any, name: Any) -> None: ...
    def save(self) -> None: ...

def convert_openpyxl_to_qtmodel(px_worksheet: Any, model_type: Any = ..., header: bool = ...): ...
