from test.framework.base_unit_test_case import BaseUnitTestCase

class TestMasterConfigLoader(BaseUnitTestCase):
    def test_configure_default_sets_protocol_scheme_to_http(self) -> None: ...
    def test_configure_postload_sets_protocol_scheme_to_https(self) -> None: ...
