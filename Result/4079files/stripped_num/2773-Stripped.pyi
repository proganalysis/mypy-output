# (generated with --quick)

from typing import Any, Mapping, NoReturn, Optional, Tuple, TypeVar, Union

argparse: module
collections: module
datetime: module
exifread: Any
hash_cache: HashCache
hashlib: module
logger: logging.Logger
logging: module
os: module
queue: module
re: module
shutil: module
sys: module
threading: module
time: module
watchdog: Any

_T0 = TypeVar('_T0')

class BadExifTimestampError(Exception): ...

class EventHandler(Any):
    shared_queue: Any
    target_folder: Any
    def __init__(self, shared_queue, target_folder) -> None: ...
    def on_created(self, event) -> None: ...
    def on_modified(self, event) -> None: ...
    def on_moved(self, event) -> None: ...

class HashCache:
    __doc__: str
    hashes: Mapping[str, Tuple[set, dict]]
    def __init__(self) -> None: ...
    def _add_file(self, path) -> None: ...
    @staticmethod
    def _files_in_folder(folder_path) -> list: ...
    @staticmethod
    def _hash(path) -> str: ...
    @staticmethod
    def _target_folder(path) -> Any: ...
    def has_file(self, target_folder, path) -> bool: ...

class MissingExifTimestampError(Exception): ...

class MoveFileThread(threading.Thread):
    dest_folder: Any
    is_running: bool
    shared_queue: Any
    def __init__(self, shared_queue, dest_folder) -> None: ...
    def run(self) -> NoReturn: ...
    def stop(self) -> None: ...

def basename_from_datetime(dt) -> Any: ...
def creation_date(path) -> Any: ...
def dest_path(root_folder, path) -> Any: ...
def exif_creation_date(path) -> Optional[datetime.datetime]: ...
def exif_creation_timestamp(path) -> str: ...
def exif_timestamp_to_datetime(ts) -> datetime.datetime: ...
def file_creation_date(path) -> datetime.datetime: ...
def filename_from_datetime(dt, path) -> Any: ...
def folder_from_datetime(dt) -> Any: ...
def is_valid_filename(path) -> bool: ...
def main(argv) -> int: ...
def move_file(root_folder, path) -> None: ...
def parse_args(argv) -> argparse.Namespace: ...
def path_from_datetime(root_folder, dt, path) -> Any: ...
def resolve_duplicate(path: _T0) -> Union[str, _T0]: ...
def run(src_folder, dest_folder) -> Any: ...
