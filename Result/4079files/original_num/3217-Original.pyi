# (generated with --quick)

from typing import Any

BlsKeyManager: Any
os: module

class BlsKeyManagerFile(Any):
    BLS_KEYS_DIR_MODE: int
    BLS_KEYS_DIR_NAME: str
    BLS_PK_FILE_MODE: int
    BLS_PK_FILE_NAME: str
    BLS_SK_FILE_MODE: int
    BLS_SK_FILE_NAME: str
    _bls_keys_dir: str
    _keys_dir: Any
    def _BlsKeyManagerFile__load_from_file(self, name) -> str: ...
    def _BlsKeyManagerFile__save_to_file(self, key: str, name, mode) -> None: ...
    def __init__(self, keys_dir) -> None: ...
    def _init_dirs(self) -> None: ...
    def _load_public_key(self) -> str: ...
    def _load_secret_key(self) -> str: ...
    def _save_public_key(self, pk: str) -> None: ...
    def _save_secret_key(self, sk: str) -> None: ...
