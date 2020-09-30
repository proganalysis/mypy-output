# (generated with --quick)

from typing import Any

CScript: Any
OP_0: Any
bytes_to_hex_str: Any
chars: str
hash160: Any
hash256: Any
hex_str_to_bytes: Any
segwit_addr: Any
sha256: Any

def byte_to_base58(b, version) -> str: ...
def check_key(key) -> Any: ...
def check_script(script) -> Any: ...
def key_to_p2pkh(key, main = ...) -> Any: ...
def key_to_p2sh_p2wpkh(key, main = ...) -> Any: ...
def key_to_p2wpkh(key, main = ...) -> Any: ...
def keyhash_to_p2pkh(hash, main = ...) -> str: ...
def program_to_witness(version, program, main = ...) -> Any: ...
def script_to_p2sh(script, main = ...) -> Any: ...
def script_to_p2sh_p2wsh(script, main = ...) -> Any: ...
def script_to_p2wsh(script, main = ...) -> Any: ...
def scripthash_to_p2sh(hash, main = ...) -> str: ...
