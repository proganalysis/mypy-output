from django.test import TestCase

class TestManagementGenericFunctions(TestCase):
    test_image_path: str = ...
    def setUp(self) -> None: ...
    def test_markdown_generation(self) -> None: ...
    def test_image_upload(self) -> None: ...
