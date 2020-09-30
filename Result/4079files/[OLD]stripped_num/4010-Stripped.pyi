# (generated with --quick)

import pathlib
import subprocess
from typing import Any, Type

Path: Type[pathlib.Path]
Popen: Type[subprocess.Popen]
argparse: module
args: argparse.Namespace
check_running: Any
get_homedir: Any
parser: argparse.ArgumentParser
time: module

def check_all(stop = ...) -> None: ...
def launch_all() -> None: ...
def launch_cache(storage_directory = ...) -> None: ...
def shutdown_cache(storage_directory = ...) -> None: ...
def stop_all() -> None: ...
