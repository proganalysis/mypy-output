from typing import Any

TRIES: Any

def normalize_name(name: Any): ...
def load_trie(filename: Any): ...
def get_trie_value(trie: Any, key: Any): ...
def name_to_code(category: Any, name: Any, language: str=...) -> Any: ...
def code_to_names(category: Any, code: Any): ...
