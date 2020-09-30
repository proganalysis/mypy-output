from typing import Any

class Context:
    project_adapter: Any = ...
    entrypoint_text: Any = ...
    run_text: Any = ...
    externalbasis: str = ...
    base_text: Any = ...
    def __init__(self) -> None: ...

class CommandLineInterface:
    context: Any = ...
    pkg_install_cmds: Any = ...
    def __init__(self) -> None: ...
    def _os_install(self, package_file: Any): ...
    def _lang_install(self, package_file: Any): ...
    def pave_profile(self) -> None: ...
    def pave_project(self) -> None: ...
    def pave_community(self) -> None: ...
    def ensure_config(self) -> None: ...
    def write_dockerfile(self) -> None: ...
    def _assemble_dockerfile(self): ...
    def build(self) -> None: ...
    def run(self) -> None: ...
