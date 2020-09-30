import unittest

class TestLogger(unittest.TestCase):
    VERY_FAR_IN_TIME: int = ...
    def setUp(self) -> None: ...
    def test_connect_to_database(self) -> None: ...
    def test_double_connect_to_database(self) -> None: ...
    def test_invalid_db_path(self) -> None: ...
    def test_set_log_level(self) -> None: ...
    def test_set_log_level_numeric(self) -> None: ...
    def test_log(self) -> None: ...
    def test_log_stderr(self) -> None: ...
    def test_get_logs_by_level(self) -> None: ...
    def test_get_logs_by_category(self) -> None: ...
    def test_get_logs_by_date(self) -> None: ...
    @staticmethod
    def load_logs() -> None: ...