# (generated with --quick)

from typing import Any

file_checksum: Any
file_content_type: Any
parse_content_disposition: Any
pytest: Any
read_in_chunks: Any
test_parse_content_disposition: Any
validate_file_or_path: Any

def __getattr__(name) -> Any: ...
def test_file_checksum_filename(text_filename) -> None: ...
def test_file_checksum_stream(binary_stream) -> None: ...
def test_file_content_type(text_filename, binary_stream) -> None: ...
def test_read_in_chunks(binary_stream) -> None: ...
def test_validate_file_or_path(text_filename, binary_stream) -> None: ...
