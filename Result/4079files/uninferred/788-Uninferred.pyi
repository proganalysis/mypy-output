from typing import Any, Optional

def lkworkspace(wsdir: Any) -> None: ...
def make_commandfile(job_id: Any, commands: Any) -> None: ...
def debspawn_run_commandfile(jlog: Any, suite: Any, arch: Any, build_dir: Any, artifacts_dir: Any, command_script: Any, header: Optional[Any] = ..., allow_dev_access: bool = ...): ...