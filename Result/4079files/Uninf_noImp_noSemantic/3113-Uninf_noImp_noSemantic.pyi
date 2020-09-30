from typing import Any

def command_type(request: Any): ...
def system_type(request: Any): ...
def auth_type(request: Any): ...
def valid_payload(request: Any): ...
def valid_payload_bytes(valid_payload: Any): ...
def invalid_payload_type(request: Any): ...
def bytes_larger_than_maxdata(): ...
def bytes_larger_than_connect_auth_max_data(): ...
def str_larger_than_connect_auth_max_data(): ...
def random_header(command_type: Any, random_arg0: Any, random_arg1: Any, random_data_length: Any, random_data_checksum: Any, command_type_magic: Any): ...
def random_header_bytes(random_header: Any): ...
def command_type_magic(command_type: Any): ...
def random_arg0(): ...
def random_arg1(): ...
def random_data_length(): ...
def random_data_checksum(): ...
def random_serial(): ...
def random_banner(): ...
def random_signature(): ...
def random_rsa_public_key(): ...
def random_local_id(): ...
def random_remote_id(): ...
def random_destination(): ...
def random_bytes(length: int = ...): ...
def random_hex_str(length: int = ...): ...
def random_str(length: int = ..., alphabet: Any = ...): ...
def random_int(low: int = ..., high: Any = ...): ...