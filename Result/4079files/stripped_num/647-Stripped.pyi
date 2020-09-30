# (generated with --quick)

from typing import Any, Tuple

ExplorationPolicy: Any
abc: module

class ExplorationStrategy(object, metaclass=abc.ABCMeta):
    @abstractmethod
    def get_action(self, t, observation, policy, **kwargs) -> Any: ...
    def reset(self) -> None: ...

class PolicyWrappedWithExplorationStrategy(Any):
    es: Any
    policy: Any
    t: Any
    def __init__(self, exploration_strategy, policy) -> None: ...
    def get_action(self, *args, **kwargs) -> Any: ...
    def reset(self) -> None: ...
    def set_num_steps_total(self, t) -> None: ...

class RawExplorationStrategy(ExplorationStrategy):
    def get_action(self, t, policy, *args, **kwargs) -> Tuple[Any, Any]: ...
    @abstractmethod
    def get_action_from_raw_action(self, action, **kwargs) -> Any: ...