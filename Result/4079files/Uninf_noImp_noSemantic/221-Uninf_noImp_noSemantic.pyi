from typing import Any

class ColorDummy:
    def __getattr__(self, name: Any): ...

p: Any
SHARED_IGNORED_RESOURCES: Any
CLIENT_IGNORED_RESOURCES: Any
SERVER_IGNORED_RESOURCES: Any

def main() -> None: ...
def wipe_bin() -> None: ...
def build_windows() -> None: ...
def build_macos() -> None: ...
def build_linux() -> None: ...
def copy_resources(target: Any, zipf: Any, server: Any) -> None: ...
def do_resource_copy(target: Any, source: Any, zipf: Any, server: Any) -> None: ...
def zip_entry_exists(zipf: Any, name: Any): ...
def copy_dir_into_zip(directory: Any, basepath: Any, zipf: Any) -> None: ...
def copy_content_assemblies(target: Any, zipf: Any, server: Any) -> None: ...
def copy_godot_scenes() -> None: ...
def copy_dir_or_file(src: Any, dst: Any) -> None: ...
