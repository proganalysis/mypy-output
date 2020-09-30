# (generated with --quick)

from typing import Any

datetime: module
sqlite3: module

class libJournal:
    db_location: Any
    entry_number: int
    def __init__(self) -> None: ...
    @staticmethod
    def _libJournal__entries_iterate(entry_dict) -> None: ...
    @staticmethod
    def _libJournal__get_date() -> str: ...
    @staticmethod
    def _libJournal__get_time() -> str: ...
    def _libJournal__set_latest_entry_number(self) -> None: ...
    @staticmethod
    def create_db(db_name) -> None: ...
    def delete_by_number(self, entry_number) -> None: ...
    def entries_all(self) -> list: ...
    def entry_new(self, entry_title, entry_content) -> None: ...
    def most_recent_entry(self) -> Any: ...
    def read_by_date(self, entry_date, entry_location) -> Any: ...
    def read_by_number(self, entry_number) -> Any: ...
    def read_by_title(self, entry_name, entry_location) -> Any: ...
    def search_by_date(self, entry_date) -> list: ...
    def search_by_number(self, entry_number) -> list: ...
    def search_by_title(self, entry_title) -> list: ...
    def set_db_location(self, db_name) -> None: ...
    @staticmethod
    def setup_db(db_name) -> None: ...
