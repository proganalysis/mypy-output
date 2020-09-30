import numpy as np
from pyshgp.gp.genome import Genome
from pyshgp.push.atoms import CodeBlock
from typing import Any, Union

class Individual:
    __slots__: Any = ...
    _genome: Any = ...
    _program: Any = ...
    _error_vector: Any = ...
    _total_error: Any = ...
    _error_vector_bytes: Any = ...
    def __init__(self, genome: Genome=...) -> None: ...
    @property
    def genome(self) -> Genome: ...
    @genome.setter
    def genome(self, value: Genome) -> Any: ...
    @property
    def program(self) -> CodeBlock: ...
    @program.setter
    def program(self, value: CodeBlock) -> Any: ...
    @property
    def error_vector(self) -> np.ndarray: ...
    @error_vector.setter
    def error_vector(self, error_vector: np.ndarray) -> Any: ...
    @property
    def total_error(self) -> Union[np.int64, np.float64]: ...
    @total_error.setter
    def total_error(self, value: Union[np.int64, np.float64]) -> Any: ...
    @property
    def error_vector_bytes(self): ...
    @error_vector_bytes.setter
    def error_vector_bytes(self, value: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
