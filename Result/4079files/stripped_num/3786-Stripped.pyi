# (generated with --quick)

from typing import Any, Generator, List

ParserWithRecovery: Any
addsitedir: Any
common: Any
debug: Any
exec_function: Any
glob: module
load_parser: Any
memoize_default: Any
os: module
save_parser: Any
sys: module
sys_path_with_modifications: Any
tree: Any
unicode: Any

def _check_module(evaluator, module) -> list: ...
def _detect_django_path(module_path) -> list: ...
def _execute_code(module_path, code) -> list: ...
def _get_buildout_scripts(module_path) -> List[str]: ...
def _get_parent_dir_with_file(path, filename) -> Any: ...
def _get_paths_from_buildout_script(evaluator, buildout_script) -> Generator[Any, Any, None]: ...
def _get_sys_path_with_egglinks(sys_path) -> list: ...
def _get_venv_path_dirs(venv) -> List[nothing]: ...
def _get_venv_sitepackages(venv) -> str: ...
def _paths_from_assignment(evaluator, expr_stmt) -> Generator[Any, Any, None]: ...
def _paths_from_list_modifications(module_path, trailer1, trailer2) -> list: ...
def get_venv_path(venv) -> List[str]: ...
def traverse_parents(path) -> Generator[Any, Any, None]: ...
