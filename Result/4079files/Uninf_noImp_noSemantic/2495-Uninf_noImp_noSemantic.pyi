import qubes.tests.storage
from typing import Any, Optional

class TestApp(qubes.Qubes):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class ReflinkMixin:
    test_dir: Any = ...
    def setUp(self, fs_type: str = ...) -> None: ...
    def test_000_copy_file(self) -> None: ...
    def test_001_create_and_resize_files_and_update_loopdevs(self) -> None: ...

class TC_10_ReflinkPool(qubes.tests.QubesTestCase):
    test_dir: str = ...
    app: Any = ...
    pool: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_012_import_data_empty(self) -> None: ...

class TC_00_ReflinkOnBtrfs(ReflinkMixin, qubes.tests.QubesTestCase):
    ficlone_supported: bool = ...
    def setUp(self) -> None: ...

class TC_01_ReflinkOnExt4(ReflinkMixin, qubes.tests.QubesTestCase):
    ficlone_supported: bool = ...
    def setUp(self) -> None: ...

def setup_loopdev(img: Any, cleanup_via: Optional[Any] = ...): ...
def detach_loopdev(dev: Any) -> None: ...
def get_fs_type(directory: Any): ...
def mkdir_fs(directory: Any, fs_type: Any, accessible: bool = ..., max_size: Any = ..., cleanup_via: Optional[Any] = ...) -> None: ...
def rmtree_fs(directory: Any) -> None: ...
def get_blockdev_size(dev: Any): ...
def reflink_update_loopdev_sizes(img: Any) -> None: ...
def cmd(*argv: Any): ...
