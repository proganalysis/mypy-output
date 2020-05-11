# (generated with --quick)

import itertools
import pathlib
from typing import Any, Dict, Generator, Iterator, Optional, Tuple, Type, TypeVar

Path: Type[pathlib.Path]
appdirs: Any
chain: Type[itertools.chain]
cloud_warning_flag: int
io: module
is_exe: bool
multitiles: Any
multitilestrides: Any
os: module
sys: module
tempfile: module

_N = TypeVar('_N', int, float)

class Chests:
    endpos: Optional[int]
    path: Any
    pos: Any
    def __init__(self, path, pos) -> None: ...
    def __iter__(self) -> Generator[Any, Any, None]: ...
    def __len__(self) -> int: ...

class NPCs:
    endpos: Optional[int]
    len: int
    path: Any
    pos: Any
    def __init__(self, path, pos) -> None: ...
    def __iter__(self) -> Generator[Any, Any, None]: ...
    def __len__(self) -> int: ...

class Signs:
    endpos: Optional[int]
    path: Any
    pos: Any
    def __init__(self, path, pos) -> None: ...
    def __iter__(self) -> Generator[Any, Any, None]: ...
    def __len__(self) -> int: ...

class Tiles:
    endpos: Optional[int]
    h: Any
    path: Any
    pos: Any
    w: Any
    def __init__(self, path, pos, w, h) -> None: ...
    def __iter__(self) -> Generator[Any, Any, None]: ...
    def __len__(self) -> Any: ...

class Trail:
    path: Any
    pos: Any
    def __init__(self, path, pos) -> None: ...
    def get(self) -> Tuple[Any, Any, Any]: ...

class World:
    chestpos: Any
    chests: Chests
    header: Any
    npcpos: Any
    npcs: NPCs
    path: Any
    signpos: Any
    signs: Signs
    tilepos: int
    tiles: Tiles
    def __init__(self, path) -> None: ...
    def make_split(self) -> None: ...
    def ready_chests(self) -> None: ...
    def ready_npcs(self) -> None: ...
    def ready_signs(self) -> None: ...

def __getattr__(name) -> Any: ...
def count(start: _N = ..., step: _N = ...) -> Iterator[_N]: ...
def get_content(f, layers = ...) -> tuple: ...
def get_multis() -> Dict[str, Any]: ...
def get_myterraria() -> pathlib.Path: ...
def get_next_world(name = ...) -> Optional[pathlib.Path]: ...
def get_players() -> Generator[nothing, Any, None]: ...
def get_remote_terraria_dirs(sub_dir = ...) -> Generator[pathlib.Path, Any, None]: ...
def get_steamdir() -> pathlib.Path: ...
def get_worlds(source = ...) -> Generator[nothing, Any, None]: ...
def write_tiles(surface, header, walls = ..., report = ..., overwrite_no_mt = ..., callback = ...) -> tempfile.SpooledTemporaryFile[nothing]: ...
