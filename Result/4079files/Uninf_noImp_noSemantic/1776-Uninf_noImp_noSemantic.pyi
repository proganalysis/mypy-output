import numpy as np
from typing import Any, List
from yarll.memory.experiences_memory import ExperiencesMemory

class EnvRunner:
    env: Any = ...
    policy: Any = ...
    state: Any = ...
    features: Any = ...
    config: Any = ...
    episode_steps: int = ...
    episode_reward: float = ...
    n_episodes: int = ...
    state_preprocessor: Any = ...
    summary_writer: Any = ...
    normalize_states: Any = ...
    rms: Any = ...
    def __init__(self, env: Any, policy: Any, config: dict, normalize_states: Any=..., state_preprocessor: Any=..., summary_writer: Any=...) -> None: ...
    def choose_action(self, state: np.ndarray) -> Any: ...
    def normalize(self, state: np.ndarray) -> np.ndarray: ...
    def reset_env(self) -> None: ...
    def step_env(self, action: Any): ...
    def get_steps(self, n_steps: int, reset: bool=..., stop_at_trajectory_end: bool=..., render: bool=...) -> ExperiencesMemory: ...
    def get_trajectory(self, stop_at_trajectory_end: bool=..., render: bool=...) -> ExperiencesMemory: ...
    def get_trajectories(self, stop_at_trajectory_end: bool=..., render: bool=...) -> List[ExperiencesMemory]: ...