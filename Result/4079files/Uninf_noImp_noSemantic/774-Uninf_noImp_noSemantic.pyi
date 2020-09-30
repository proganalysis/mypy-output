from typing import Any, List, Optional, Tuple

class Node:
    state: Any = ...
    action: Any = ...
    cost: Any = ...
    parent: Any = ...
    def __init__(self, state: Tuple[int, int], action: str, cost: int, parent: Any) -> None: ...
    def parent_state(self): ...
    def get_path(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def __str__(self): ...

class SearchProblem:
    def getStartState(self) -> None: ...
    def isGoalState(self, state: Any) -> None: ...
    def getSuccessors(self, state: Any) -> None: ...
    def getCostOfActions(self, actions: Any) -> None: ...

def tinyMazeSearch(problem: Any): ...
def graph_search(problem: Any, frontier: Any) -> List[str]: ...
def depthFirstSearch(problem: Any): ...
def breadthFirstSearch(problem: Any): ...
def uniformCostSearch(problem: Any): ...
def nullHeuristic(state: Any, problem: Optional[Any] = ...): ...
def manhattanHeuristic(state: Any, problem: Optional[Any] = ...): ...
def aStarSearch(problem: Any, heuristic: Any = ...): ...
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
