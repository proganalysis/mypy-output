from typing import Any

class Node:
    data: Any = ...
    left: Any = ...
    right: Any = ...
    def __init__(self, val: Any) -> None: ...

class BinaryTree:
    head: Any = ...
    def __init__(self) -> None: ...
    def insert(self, item: Any) -> None: ...
    def add(self, node: Any, val: Any) -> None: ...

def preorder(hash_map: Any, level: Any, head: Any) -> None: ...