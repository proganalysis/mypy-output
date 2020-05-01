# (generated with --quick)

import itertools
from typing import Any, Dict, Generator, Type

DeferredType: Any
PolygraphField: Any
PolygraphInputValue: Any
PolygraphType: Any
Schema: Any
StrictDict: Any
attrib: Any
attrs: Any
chain: Type[itertools.chain]
evolve: Any

class TypeMap(Dict[TypeName, Any]):
    def __init__(self, val: Dict[TypeName, Any]) -> None: ...

class TypeName(str):
    def __init__(self, val: str) -> None: ...

class UnresolvedType(Any):
    def __init__(self, val) -> None: ...

def build_schema(query_type, mutation_type = ..., additional_types = ...) -> Any: ...
def collect_type_names(types) -> Any: ...
def undefer_field(field, type_map) -> Any: ...
def undefer_input_value(input_value, type_map) -> Any: ...
def undefer_subtypes(type_, type_map) -> Any: ...
def undefer_type(type_, type_map) -> Any: ...
def visit_types(types, visited = ...) -> Generator[Any, Any, None]: ...