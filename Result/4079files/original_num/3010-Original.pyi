# (generated with --quick)

from typing import Callable, Dict

hashlib: module
json: module

def get_filters() -> Dict[str, Callable]: ...
def hash(symbol, hash_type = ...) -> str: ...
def identifier(s) -> str: ...
def jsonify(symbol) -> str: ...
def lower_first(s) -> str: ...
def path(symbol) -> str: ...
def upper_first(s) -> str: ...
