import requests_mock
from typing import Any
from unittest.case import TestCase

class PackageAPISectionTests(TestCase):
    papi: Any = ...
    def __init__(self, *args: Any) -> None: ...
    def test_show(self, rmock: requests_mock.Mocker) -> None: ...