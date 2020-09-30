# (generated with --quick)

from typing import Any
import unittest.case
import unittest.mock

ApiContent: Any
HtmlContent: Any
Mock: Any
gen_entries_by_ids_with_futures: Any
os: module
patch: unittest.mock._patcher
sys: module
unittest: module

class ApiContentTest(unittest.case.TestCase):
    content: Any
    mock_apisign: Any
    mock_get_json: Any
    def test_gen_entries_if_correct_incrementing_and_output(self) -> None: ...
    def test_gen_entries_with_ids_if_correct_output(self) -> None: ...
    def test_get_json_for_valuerror_when_no_url_matched_or_no_id(self) -> None: ...
    def test_get_json_if_correct_urls_are_passed_to_requester_when_entry_url(self) -> None: ...
    def test_get_json_if_correct_urls_are_passed_to_requester_when_fav_url(self) -> None: ...
    def test_get_json_if_correct_value_is_returned(self) -> None: ...
    def test_get_json_when_valueerror_raised_from_requester(self) -> None: ...
    def test_init_urls(self) -> None: ...
    def test_submit_to_executor_when_page_is_none(self) -> None: ...
    def test_submit_to_executor_when_page_is_not_none(self) -> None: ...

class GenEntriesByIdsWithFuturesTest(unittest.case.TestCase):
    def test_if_only_true_values_are_returned(self) -> None: ...
    def test_if_return_values_are_correct(self) -> None: ...

class HtmlContentTest(unittest.case.TestCase):
    content: Any
    mock_get: Any
    def test_gen_html_entries_by_ids_if_correct_len(self) -> None: ...
    def test_gen_html_entries_by_ids_if_correct_output(self) -> None: ...
    def test_gen_html_entries_by_ids_if_request_failed(self) -> None: ...
    def test_get_entry_check_call(self) -> None: ...
    def test_get_entry_response_not_200(self) -> None: ...
    def test_get_entry_response_ok(self) -> None: ...