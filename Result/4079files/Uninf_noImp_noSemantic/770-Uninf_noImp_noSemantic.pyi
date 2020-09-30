from typing import Any, Optional
from varapp.common.utils import random_string as random_string
from varapp.models.users import VariantsDb

logger: Any
GEMINI_DB_PATH: Any
TEST_PATH: Any

def table_names(dbname: Any): ...
def connection_has_tables(dbname: Any, N: int = ...): ...
def inspect_db(dbname: str = ...): ...
def is_sqlite3(filename: Any): ...
def is_on_disk(filename: Any, path: Any = ...): ...
def db_name_from_filename(filename: Any, fallback: Optional[Any] = ...): ...
def vdb_full_path(vdb: VariantsDb) -> Any: ...
def add_db_to_settings(dbname: Any, filename: Any, gemini_path: Any = ...) -> None: ...
def remove_db_from_settings(dbname: Any) -> None: ...
def remove_db_from_cache(dbname: Any) -> None: ...
def add_db(vdb: VariantsDb) -> Any: ...
def remove_db(vdb: VariantsDb) -> Any: ...
def is_test_vdb(vdb: VariantsDb) -> Any: ...
def is_source_updated(vdb: VariantsDb, path: Any=..., warn: Any=...) -> Any: ...
def is_valid_vdb(vdb: VariantsDb, path: Any=...) -> Any: ...
def is_hash_changed(vdb: VariantsDb, path: Any=..., warn: Any=...) -> Any: ...