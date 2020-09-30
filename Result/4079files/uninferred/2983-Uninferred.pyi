from typing import Any, Optional

class Configuration:
    config_path: Any = ...
    config: Any = ...
    def __init__(self, filename: Optional[Any] = ...) -> None: ...
    def get_option(self, section: Any, key: Any, default: Optional[Any] = ...): ...
    def db_connection(self, dbname: Any): ...
    @property
    def flora(self): ...
    @property
    def kit_fixups(self): ...
    @property
    def gentoo_staging(self): ...
    def base_url(self, repo: Any): ...
    def branch(self, key: Any): ...
    @property
    def source_trees(self): ...
    @property
    def dest_trees(self): ...
