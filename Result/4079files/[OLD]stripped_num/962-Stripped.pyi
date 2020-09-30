# (generated with --quick)

from typing import Any

DOSection: Any
DO_FOR_TEST: str
Destination: Any
PdfFileMerger: Any
PdfFileReader: Any
PdfFileWriter: Any
RESULTS_FOLDER: str
SAMPLE_FOLDER: str
box_titles: Any
constants: Any
dom_urls: Any
os: module
requests: module
shutil: module
utils: Any

def assemble_from_pages(raw_url, filename, tmpdir = ..., begin = ..., end = ...) -> None: ...
def assemble_pages_from_list(filename, pages_list, work_dir) -> None: ...
def download_from_id(edi_id, filename) -> None: ...
def download_from_raw_url(raw_url, filename) -> None: ...
def download_pages_from_id(edi_id, work_dir, begin = ..., end = ...) -> None: ...
def download_pages_from_raw_url(raw_url, work_dir) -> None: ...
def download_url_from_id(edi_id) -> Any: ...
def download_url_from_raw_url(raw_url) -> Any: ...
def get_sections(pdf_reader) -> list: ...
def main() -> None: ...
def split_domrj_sections(filepath, workdir) -> None: ...
def write_section(pdf_reader, section, output = ...) -> None: ...
