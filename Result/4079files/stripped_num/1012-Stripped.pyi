# (generated with --quick)

import tests
from typing import Any, Type

Pyas2TestCase: Type[tests.Pyas2TestCase]
as2: Any

class TestBasic(tests.Pyas2TestCase):
    org: Any
    partner: Any
    def find_org(self, as2_id) -> Any: ...
    def find_partner(self, as2_id) -> Any: ...
    def test_compressed_message(self) -> None: ...
    def test_encrypted_message(self) -> None: ...
    def test_encrypted_signed_compressed_message(self) -> None: ...
    def test_encrypted_signed_message(self) -> None: ...
    def test_encrypted_signed_message_dos(self) -> None: ...
    def test_plain_message(self) -> None: ...
    def test_signed_message(self) -> None: ...
