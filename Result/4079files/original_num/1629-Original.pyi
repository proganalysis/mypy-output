# (generated with --quick)

from typing import Any, Iterator, Optional

FLAGS: Any
_GPUS: Optional[tuple]
device_lib: Any
flags: Any
glob: module
np: module
os: module
re: module
tf: Any

def average_gradients(tower_grads) -> Any: ...
def find_latest_checkpoint(dir, glob_term = ...) -> Any: ...
def get_available_gpus() -> Any: ...
def get_config() -> Any: ...
def get_latest_global_step(dir) -> Any: ...
def get_latest_global_step_in_subdir(dir) -> Any: ...
def getter_ema(ema, getter, name, *args, **kwargs) -> Any: ...
def gpu(x) -> str: ...
def ilog2(x) -> int: ...
def model_vars(scope = ...) -> Any: ...
def para_cat(fn, *args) -> Any: ...
def para_list(fn, *args) -> Iterator[nothing]: ...
def para_mean(fn, *args) -> Any: ...
def setup_tf() -> None: ...
def smart_shape(x) -> list: ...
