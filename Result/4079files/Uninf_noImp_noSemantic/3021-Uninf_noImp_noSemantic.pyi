from .base import BaseTestRunner

class TestUtils(BaseTestRunner):
    def test_homify(self) -> None: ...
    def test_hex_to_dec(self) -> None: ...
    def test_wei_to_ether(self) -> None: ...
    def test_ether_to_wei(self) -> None: ...
    def test_ether_to_gwei(self) -> None: ...
    def test_create_default_logger(self) -> None: ...
