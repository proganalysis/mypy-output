from typing import Any, Optional

_GPUS: Any
FLAGS: Any

def get_config(): ...
def setup_tf() -> None: ...
def smart_shape(x: Any): ...
def ilog2(x: Any): ...
def find_latest_checkpoint(dir: Any, glob_term: str = ...): ...
def get_latest_global_step(dir: Any): ...
def get_latest_global_step_in_subdir(dir: Any): ...
def getter_ema(ema: Any, getter: Any, name: Any, *args: Any, **kwargs: Any): ...
def model_vars(scope: Optional[Any] = ...): ...
def gpu(x: Any): ...
def get_available_gpus(): ...
def average_gradients(tower_grads: Any): ...
def para_list(fn: Any, *args: Any): ...
def para_mean(fn: Any, *args: Any): ...
def para_cat(fn: Any, *args: Any): ...
