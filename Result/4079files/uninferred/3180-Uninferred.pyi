from typing import Any

test_objective: Any
test_objective_noisy: Any

def test_variational_objective_value() -> None: ...
def test_variational_objective_noise() -> None: ...
def test_variational_objective_noise_bounds() -> None: ...
def test_variational_objective_is_abstract_cant_instantiate() -> None: ...
def test_variational_objective_is_abstract_must_implement() -> None: ...
def test_variational_objective_is_abstract_can_implement() -> None: ...
