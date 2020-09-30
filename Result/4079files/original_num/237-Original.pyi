# (generated with --quick)

import _ast
import collections
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union

Attribute: Any
Bool: Any
GeneratorMock: Any
OrderedDict: Type[collections.OrderedDict]
Sort: Any
SortMock: Any
TermMock: Any
TermMockManager: Any
TranslationError: Any
ast: module
astunparse: Any
generator: Any
inspect: module
make_term_from_call: Any
operation: Any
var: Any

_T_OperationParser = TypeVar('_T_OperationParser', bound=_OperationParser)

class Translator(object):
    axioms: Dict[Any, List[Dict[str, Any]]]
    generators: set
    operations: set
    sorts: set
    def _parse_operation(self, operation, register_axiom) -> None: ...
    def post_translate(self) -> None: ...
    def pre_translate(self) -> None: ...
    def register(self, obj) -> None: ...
    def register_axiom(self, operation, guards, matchs, return_value) -> None: ...
    def translate(self) -> None: ...

class _Dereferencer(ast.NodeTransformer):
    references: Any
    def __init__(self, references) -> None: ...
    def visit_Name(self, node) -> Any: ...

class _OperationParser(ast.NodeVisitor):
    comparison_operators: Dict[Type[Union[_ast.Eq, _ast.Gt, _ast.GtE, _ast.In, _ast.Lt, _ast.LtE, _ast.NotEq]], str]
    fn_scope: dict
    locals: Any
    operation: Any
    register_axiom: Any
    stack: Any
    def __init__(self, register_axiom, operation, stack = ..., local_vars = ...) -> None: ...
    def _dnf(self, node) -> Any: ...
    def _make_subparser(self: _T_OperationParser, stack) -> _T_OperationParser: ...
    def parse_condition(self, node, var_manager) -> Optional[Tuple[Optional[Tuple[Any, str, Any]], Optional[Tuple[Any, Any]]]]: ...
    def parse_conditions(self, var_manager) -> Tuple[list, dict]: ...
    def parse_expr(self, node, var_manager) -> Any: ...
    def parse_object(self, obj) -> Any: ...
    def substitute(self, term, name, substitution) -> Any: ...
    def visit_Assign(self, node) -> None: ...
    def visit_If(self, node) -> None: ...
    def visit_Return(self, node) -> None: ...

class _TransformIfExpReturn(ast.NodeTransformer):
    def visit_Return(self, node) -> Any: ...

def _unindent(src) -> str: ...
