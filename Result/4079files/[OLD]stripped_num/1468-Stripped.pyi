# (generated with --quick)

import collections
from typing import Any, Generator, NoReturn, Optional, Tuple, Type, TypeVar

OrderedDict: Type[collections.OrderedDict]
io: module
json: module

TypeLike = TypeVar('TypeLike')
_T1 = TypeVar('_T1')

class MarshalModel:
    _attr_tree: Any
    _attrs: Optional[collections.OrderedDict]
    _iterable: bool
    _obj: None
    _objs: list
    _raw: Any
    def __init__(self) -> None: ...
    def __iter__(self) -> NoReturn: ...
    def __next__(self) -> Generator[nothing, Any, nothing]: ...
    @classmethod
    def _convert_annot_type_tree(cls, annots) -> collections.OrderedDict: ...
    @classmethod
    def _create_attr_info(cls, obj) -> Tuple[collections.OrderedDict, Any]: ...
    @staticmethod
    def _get_attribute_list(typ) -> list: ...
    @classmethod
    def _get_root(cls, typ) -> Any: ...
    @staticmethod
    def _has_nested_type(typ) -> bool: ...
    @staticmethod
    def _has_public_attribute(typ) -> bool: ...
    @staticmethod
    def _is_any_option_union(typ) -> bool: ...
    @staticmethod
    def _is_builtin(typ) -> bool: ...
    @staticmethod
    def _is_generic(typ) -> bool: ...
    @classmethod
    def _tree_recursive(cls, typ: _T1) -> tuple: ...
    def _unmarshal(self, target, target_attr_tree, item) -> None: ...
    def _unmarshal_with_type_check(self, attr, typ) -> Any: ...
    def load_json(self, json_in, lines = ..., **kwargs) -> None: ...
    def load_json_lines(self, json_in, **kwargs) -> None: ...

class TypeCheckError(TypeError): ...
