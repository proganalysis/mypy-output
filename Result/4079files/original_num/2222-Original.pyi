# (generated with --quick)

from typing import Any, Generator, List, TypeVar

pd: Any
re: module

_T0 = TypeVar('_T0')

def get_entity_name_from_id(entity_id: _T0) -> _T0: ...
def get_mentions_info(path: str, additional_column = ...) -> Any: ...
def tac_results_reader(result_file_path, additional_column = ...) -> Generator[List[str], Any, None]: ...
def transform_tac_to_html(tac_html: str) -> str: ...
