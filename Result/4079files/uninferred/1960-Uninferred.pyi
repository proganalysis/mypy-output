from typing import Tuple

def test_any() -> None: ...
def test_numbers() -> None: ...
def test_strings() -> None: ...
def test_unions() -> None: ...
def test_tuples() -> None: ...
def test_lists() -> None: ...
def test_sets() -> None: ...
def test_dicts() -> None: ...
def test_nested_types() -> None: ...
def test_aliases() -> None: ...
def test_typevar() -> None: ...
def test_optional() -> None: ...
def test_sized() -> None: ...
def dummy_fun(a: int=..., b: str=..., c: Tuple[int, str]=...) -> int: ...
def dummy_fun_with_nonoptional(x: int, y: str=..., z: Tuple[int, str]=...) -> int: ...
def dummy_fun_with_base_collections(x: dict=..., y: tuple=...) -> int: ...
def test_args() -> None: ...
def test_dict() -> None: ...
def test_collections() -> None: ...
def test_raises_simple() -> None: ...
def test_raises_with_dictionary() -> None: ...
def test_raises_with_base_collections() -> None: ...
def test_exception_content() -> None: ...
def test_no_value_no_default() -> None: ...
def test_unknown_parameters() -> None: ...
