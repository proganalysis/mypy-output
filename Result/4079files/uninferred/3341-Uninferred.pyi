from typing import Any

class graph:
    vertices: Any = ...
    def __init__(self) -> None: ...
    def add_node(self, myid: Any) -> None: ...
    def add_edge(self, id1: Any, id2: Any) -> None: ...
    def show_graph(self) -> None: ...
    def dfs(self, root: Any): ...
    def bfs(self, root: Any): ...
    def check_bipartite(self): ...

g: Any
