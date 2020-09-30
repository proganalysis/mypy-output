from typing import Any

class JavaMethod:
    UNIT_INDENT: str = ...
    name: Any = ...
    return_type: str = ...
    access_level: str = ...
    annotation: str = ...
    inputs: Any = ...
    content_lines: Any = ...
    def __init__(self, name: str = ...) -> None: ...
    def set_name(self, name: Any) -> None: ...
    def set_return_type(self, type_name: Any) -> None: ...
    def set_access_level(self, level: Any) -> None: ...
    def add_input(self, type_name: Any, name: Any) -> None: ...
    def add_content_line(self, content: Any) -> None: ...
    def get_name(self): ...
    def get_return_type(self): ...
    def get_access_level(self): ...
    def gen_code(self, indent_amount: int = ...): ...
