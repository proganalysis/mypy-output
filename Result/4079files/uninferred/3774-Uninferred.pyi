from typing import Any

class Parent:
    __class_var: int = ...
    @classmethod
    def get_class_var(cls): ...
    @classmethod
    def set_class_var(cls, value: Any) -> None: ...
    __obj_var: Any = ...
    def __init__(self, obj_var: Any) -> None: ...
    @property
    def obj_var(self): ...
    @obj_var.setter
    def obj_var(self, value: Any) -> None: ...
    def __str__(self): ...

class Child(Parent):
    __new_obj_var: Any = ...
    def __init__(self, obj_var: Any, new_ojb_var: Any) -> None: ...
    @property
    def child_var(self): ...
    def __str__(self): ...