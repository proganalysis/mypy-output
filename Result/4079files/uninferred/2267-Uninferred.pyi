from mythril.analysis.symbolic import SymExecWrapper as SymExecWrapper
from mythril.laser.ethereum.cfg import Node as Node
from mythril.laser.ethereum.state.environment import Environment as Environment
from mythril.laser.ethereum.state.global_state import GlobalState as GlobalState
from mythril.laser.smt import Expression as Expression
from typing import Any, List, Tuple, Union

log: Any

class TaintRecord:
    stack: Any = ...
    memory: Any = ...
    storage: Any = ...
    states: Any = ...
    def __init__(self) -> None: ...
    def stack_tainted(self, index: int) -> Union[bool, None]: ...
    def memory_tainted(self, index: int) -> bool: ...
    def storage_tainted(self, index: int) -> bool: ...
    def add_state(self, state: GlobalState) -> None: ...
    def clone(self) -> TaintRecord: ...

class TaintResult:
    records: Any = ...
    def __init__(self) -> None: ...
    def check(self, state: GlobalState, stack_index: int) -> Union[bool, None]: ...
    def add_records(self, records: List[TaintRecord]) -> None: ...
    def _try_get_record(self, state: GlobalState) -> Union[TaintRecord, None]: ...

class TaintRunner:
    @staticmethod
    def execute(statespace: SymExecWrapper, node: Node, state: GlobalState, initial_stack: Any=...) -> TaintResult: ...
    @staticmethod
    def children(node: Node, statespace: SymExecWrapper, environment: Environment, transaction_stack_length: int) -> List[Node]: ...
    @staticmethod
    def execute_node(node: Node, last_record: TaintRecord, state_index: Any=...) -> List[TaintRecord]: ...
    @staticmethod
    def execute_state(record: TaintRecord, state: GlobalState) -> TaintRecord: ...
    @staticmethod
    def mutate_stack(record: TaintRecord, mutator: Tuple[int, int]) -> None: ...
    @staticmethod
    def mutate_push(op: str, record: TaintRecord) -> None: ...
    @staticmethod
    def mutate_dup(op: str, record: TaintRecord) -> None: ...
    @staticmethod
    def mutate_swap(op: str, record: TaintRecord) -> None: ...
    @staticmethod
    def mutate_mload(record: TaintRecord, op0: Expression) -> None: ...
    @staticmethod
    def mutate_mstore(record: TaintRecord, op0: Expression) -> None: ...
    @staticmethod
    def mutate_sload(record: TaintRecord, op0: Expression) -> None: ...
    @staticmethod
    def mutate_sstore(record: TaintRecord, op0: Expression) -> None: ...
    @staticmethod
    def mutate_log(record: TaintRecord, op: str) -> None: ...
    @staticmethod
    def mutate_call(record: TaintRecord, op: str) -> None: ...
    stack_taint_table: Any = ...
