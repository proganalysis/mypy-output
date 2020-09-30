# (generated with --quick)

from typing import Any, Dict, List, Type, Union
import unittest.case

ResultJob: Any
TestCase: Type[unittest.case.TestCase]

class LibBigQueryResultTestCase(unittest.case.TestCase):
    def response_example(self) -> Dict[str, Union[bool, str, Dict[str, Union[str, List[Dict[str, str]]]], List[Dict[str, List[Dict[str, str]]]]]]: ...
    def response_example_empty(self) -> Dict[str, Union[int, str, Dict[str, Union[str, List[Dict[str, str]]]], List[Dict[str, List[Dict[str, str]]]]]]: ...
    def test_convert_incoming_empty_obj(self) -> None: ...
    def test_convert_incoming_obj(self) -> None: ...
