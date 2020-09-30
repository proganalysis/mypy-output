from abc import ABCMeta, abstractmethod
from typing import Any, Optional

from_utf8: Any

def alert(info: Any) -> None: ...

class PropertyDescriptor:
    value: Any = ...
    def __init__(self, value: Optional[Any] = ...) -> None: ...
    def __get__(self, obj: Any, obj_type: Any): ...
    def __set__(self, obj: Any, value: Any) -> None: ...

class css(PropertyDescriptor):
    is_css: bool = ...

def abstract_property(func: Any): ...
def snake_case(camel_case: Any): ...

class AbstractRegisteringType(ABCMeta):
    def __init__(cls, name: Any, bases: Any, attributes: Any) -> None: ...

class SnakeNameMixin:
    @property
    def name(self): ...

class MenuAction(SnakeNameMixin, metaclass=AbstractRegisteringType):
    app: Any = ...
    def __init__(self, app: Any) -> None: ...
    def label(self) -> None: ...
    @property
    def checkable(self): ...
    @property
    def shortcut(self) -> None: ...
    @abstractmethod
    def action(self): ...
    @property
    def is_checked(self): ...

def singleton_creator(old_creator: Any): ...

class SingletonMetaclass(AbstractRegisteringType):
    def __init__(cls, name: Any, bases: Any, attributes: Any) -> None: ...

class RequiringMixin:
    require: Any = ...
    dependencies: Any = ...
    def __init__(self, app: Any) -> None: ...
    def __getattr__(self, attr: Any): ...

class Setting(RequiringMixin, SnakeNameMixin, metaclass=SingletonMetaclass):
    default_value: Any = ...
    app: Any = ...
    def __init__(self, app: Any) -> None: ...
    def value(self) -> None: ...
    def on_load(self) -> None: ...
    def on_save(self) -> None: ...
    def reset(self) -> None: ...

def decorate_or_call(operator: Any): ...
def style_tag(some_css: Any): ...
def percent_escaped(text: Any): ...

class StylerMetaclass(AbstractRegisteringType):
    def __init__(cls, name: Any, bases: Any, attributes: Any): ...

def wraps(method: Optional[Any] = ..., position: str = ...): ...

class appends_in_night_mode(PropertyDescriptor):
    appends_in_night_mode: bool = ...

class replaces_in_night_mode(PropertyDescriptor):
    replaces_in_night_mode: bool = ...

def move_args_to_kwargs(original_function: Any, args: Any, kwargs: Any): ...
