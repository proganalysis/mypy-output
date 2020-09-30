from typing import Any
from unittest import TestCase

TEMPLATE_DIRS: Any

class RequestTests(TestCase):
    def test_initialized(self) -> None: ...
    def test_get(self) -> None: ...
    def test_getitem(self) -> None: ...
    def test_get_default_value(self) -> None: ...
    def test_path_property(self) -> None: ...
    def test_path_property_stripped_last_slash(self) -> None: ...
    def test_method_name_to_uppercase(self) -> None: ...
    def test_POST_a_parameter(self) -> None: ...
    def test_POST_parameters(self) -> None: ...
    def test_GET_a_parameter(self) -> None: ...
    def test_GET_parameters(self) -> None: ...
    def test_raw_body(self) -> None: ...
    def test_raw_body_with_empty_string_content_length(self) -> None: ...
    def test_body(self) -> None: ...
    def test_json(self) -> None: ...
    def test_url(self) -> None: ...
    def test_headers(self) -> None: ...

class AcceptBestMatchTests(TestCase):
    def test_split_into_mimetype_and_priority_without_priority(self) -> None: ...
    def test_split_into_mimetype_and_priority_with_priority(self) -> None: ...
    def test_parse_and_sort_accept_header(self) -> None: ...
    def test_best_match_without_priority(self) -> None: ...
    def test_best_match_with_priority(self) -> None: ...
    def test_best_match_with_priority_and_wildcard(self) -> None: ...

class CookieTests(TestCase):
    def test_set_cookie(self) -> None: ...
    def test_set_cookie_with_max_age(self) -> None: ...
    def test_set_cookie_with_expires(self) -> None: ...
    def test_set_cookie_with_path(self) -> None: ...
    def test_cookies_property_has_nothing(self) -> None: ...
    def test_cookies_property_has_an_item(self) -> None: ...
    def test_get_cookie(self) -> None: ...
    def test_delete_cookie(self) -> None: ...
    def test_set_cookie_with_secret(self) -> None: ...
    def test_get_cookie_with_secret(self) -> None: ...
    def test_set_cookie_with_secret_in_config(self, mock_current_config: Any) -> None: ...