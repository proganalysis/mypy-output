# (generated with --quick)

from typing import Any

Client: Any
TestCase: Any
UserFactory: Any

class InternalRouteTests(Any):
    @classmethod
    def setUpTestData(cls) -> None: ...
    def test_index__logged_in__should_render_frontpage(self) -> None: ...
    def test_index_without_logging_in_should_redirect(self) -> None: ...
    def test_not_found__non_matching_url__catches_the_request(self) -> None: ...
