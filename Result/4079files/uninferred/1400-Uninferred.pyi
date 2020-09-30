from typing import Any

class ActivationFunction:
    type: str = ...
    def __call__(self, Z: Any) -> None: ...
    def __str__(self): ...
    def derivative(self, Z: Any) -> None: ...

class Sigmoid(ActivationFunction):
    type: str = ...
    __call__: Any = ...
    derivative: Any = ...

class Tanh(ActivationFunction):
    type: str = ...
    __call__: Any = ...
    derivative: Any = ...

class Sqrt(ActivationFunction):
    type: str = ...
    __call__: Any = ...
    derivative: Any = ...

class Linear(ActivationFunction):
    type: str = ...
    __call__: Any = ...
    derivative: Any = ...

class ReLU(ActivationFunction):
    type: str = ...
    __call__: Any = ...
    derivative: Any = ...

class SoftMax(ActivationFunction):
    type: str = ...
    __call__: Any = ...
    true_derivative: Any = ...
    def derivative(self, A: Any): ...

act_fns: Any