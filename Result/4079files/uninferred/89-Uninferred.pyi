from typing import Any

def get_token(client: Any, *args: Any): ...
def __get_salt(client: Any, username: Any): ...
def __get_hash_level_1(username: Any, password: Any, salt: Any): ...
def __get_hash_level_2(hash_level_1: Any): ...
