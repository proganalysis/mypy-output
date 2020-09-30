import unittest2

class Test_TestSkipping(unittest2.TestCase):
    def test_skipping(self) -> None: ...
    def test_skipping_subtests(self) -> None: ...
    def test_skipping_decorators(self) -> None: ...
    def test_skip_class(self) -> None: ...
    def test_skip_non_unittest_class_old_style(self) -> None: ...
    def test_skip_non_unittest_class_new_style(self) -> None: ...
    def test_expected_failure(self) -> None: ...
    def test_expected_failure_subtests(self) -> None: ...
    def test_unexpected_success(self) -> None: ...
    def test_unexpected_success_subtests(self) -> None: ...
    def test_skip_doesnt_run_setup(self) -> None: ...
    def test_decorated_skip(self): ...