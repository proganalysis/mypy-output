from typing import Any
from utils import get_answer as get_answer

def normpath(path: Any): ...

root_dir: str
prefix: str
texts_prefix: str
sub_file: Any
glitchEmoteExtractor: Any
glitchIsHere: Any

def defaultHandler(val: Any, filename: Any, path: Any): ...
def glitchDescriptionSpecialHandler(val: Any, filename: Any, path: Any): ...

textHandlers: Any
specialSharedPaths: Any

def parseFile(filename: Any): ...
def construct_db(assets_dir: Any): ...
def file_by_assets(assets_fname: Any, field: Any, substitutions: Any): ...
def process_label(combo: Any): ...
def prepare_to_write(database: Any): ...
def catch_danglings(target_path: Any, file_buffer: Any): ...
def write_file(filename: Any, content: Any): ...
def final_write(file_buffer: Any) -> None: ...
