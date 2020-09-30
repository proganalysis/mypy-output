from pyfastogt import run_command
from typing import Any

def print_usage() -> None: ...

class BuildSystem:
    name_: Any = ...
    cmd_line_: Any = ...
    cmake_generator_arg_: Any = ...
    policy_: Any = ...
    def __init__(self, name: Any, cmd_line: list, cmake_generator_arg: Any, policy: run_command.Policy) -> None: ...
    def cmake_generator_arg(self) -> str: ...
    def name(self) -> str: ...
    def policy(self) -> run_command.Policy: ...
    def cmd_line(self) -> list: ...

SUPPORTED_BUILD_SYSTEMS: Any

def get_supported_build_system_by_name(name: Any): ...
def print_message(progress: Any, message: Any) -> None: ...

class ProgressSaver:
    progress_min_: float = ...
    progress_max_: float = ...
    cb_: Any = ...
    def __init__(self, cb: Any) -> None: ...
    def update_progress_message_range(self, progress_min: Any, progress_max: Any, message: Any) -> None: ...
    def on_update_progress_message(self, progress: Any, message: Any) -> None: ...

class BuildRequest:
    platform_: Any = ...
    def __init__(self, platform: Any, arch_name: Any) -> None: ...
    def platform(self): ...
    def build(self, cmake_project_root_path: str, branding_options: list, dir_path: str, bs: BuildSystem, package_types: list, saver: ProgressSaver) -> Any: ...