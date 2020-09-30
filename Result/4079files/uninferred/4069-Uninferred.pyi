from antlr4.Recognizer import Recognizer as Recognizer
from antlr4.RuleContext import RuleContext as RuleContext
from typing import Any

class SemanticContext:
    NONE: Any = ...
    def eval(self, parser: Recognizer, outerContext: RuleContext) -> Any: ...
    def evalPrecedence(self, parser: Recognizer, outerContext: RuleContext) -> Any: ...

AND: Any

def andContext(a: SemanticContext, b: SemanticContext) -> Any: ...

OR: Any

def orContext(a: SemanticContext, b: SemanticContext) -> Any: ...
def filterPrecedencePredicates(collection: set) -> Any: ...

class Predicate(SemanticContext):
    ruleIndex: Any = ...
    predIndex: Any = ...
    isCtxDependent: Any = ...
    def __init__(self, ruleIndex: int=..., predIndex: int=..., isCtxDependent: bool=...) -> None: ...
    def eval(self, parser: Recognizer, outerContext: RuleContext) -> Any: ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __str__(self): ...

class PrecedencePredicate(SemanticContext):
    precedence: Any = ...
    def __init__(self, precedence: int=...) -> None: ...
    def eval(self, parser: Recognizer, outerContext: RuleContext) -> Any: ...
    def evalPrecedence(self, parser: Recognizer, outerContext: RuleContext) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...

class AND(SemanticContext):
    opnds: Any = ...
    def __init__(self, a: SemanticContext, b: SemanticContext) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def eval(self, parser: Recognizer, outerContext: RuleContext) -> Any: ...
    def evalPrecedence(self, parser: Recognizer, outerContext: RuleContext) -> Any: ...
    def __str__(self): ...

class OR(SemanticContext):
    opnds: Any = ...
    def __init__(self, a: SemanticContext, b: SemanticContext) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def eval(self, parser: Recognizer, outerContext: RuleContext) -> Any: ...
    def evalPrecedence(self, parser: Recognizer, outerContext: RuleContext) -> Any: ...
    def __str__(self): ...
