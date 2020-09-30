# (generated with --quick)

from typing import Any, Dict, Set

g: graph
random: module

class graph:
    vertices: Dict[Any, Set[int]]
    def __init__(self) -> None: ...
    def add_edge(self, id1, id2) -> None: ...
    def add_node(self, myid) -> None: ...
    def bfs(self, root) -> Any: ...
    def check_bipartite(self) -> bool: ...
    def dfs(self, root) -> Any: ...
    def show_graph(self) -> None: ...
