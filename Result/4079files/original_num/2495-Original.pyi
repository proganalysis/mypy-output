# (generated with --quick)

from typing import Any

os: module
qubes: Any
reflink: Any
shutil: module
subprocess: module
sys: module

class ReflinkMixin:
    test_dir: str
    def setUp(self, fs_type = ...) -> None: ...
    def test_000_copy_file(self) -> None: ...
    def test_001_create_and_resize_files_and_update_loopdevs(self) -> None: ...

class TC_00_ReflinkOnBtrfs(ReflinkMixin, Any):
    ficlone_supported: bool
    test_dir: str
    def setUp(self) -> None: ...

class TC_01_ReflinkOnExt4(ReflinkMixin, Any):
    ficlone_supported: bool
    test_dir: str
    def setUp(self) -> None: ...

class TC_10_ReflinkPool(Any):
    app: TestApp
    pool: Any
    test_dir: str
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_012_import_data_empty(self) -> None: ...

class TestApp(Any):
    __doc__: str
    default_pool: Any
    def __init__(self, *args, **kwargs) -> None: ...

def cmd(*argv) -> bytes: ...
def detach_loopdev(dev) -> None: ...
def get_blockdev_size(dev) -> int: ...
def get_fs_type(directory) -> str: ...
def mkdir_fs(directory, fs_type, accessible = ..., max_size = ..., cleanup_via = ...) -> None: ...
def reflink_update_loopdev_sizes(img) -> None: ...
def rmtree_fs(directory) -> None: ...
def setup_loopdev(img, cleanup_via = ...) -> str: ...
