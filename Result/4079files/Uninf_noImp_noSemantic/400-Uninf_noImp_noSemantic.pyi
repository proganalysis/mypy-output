from typing import Any

__all__: Any

def _get_change_making_matrix(c: int, n: int) -> list: ...
def _get_sets_of_coins_matrix(c: int, n: int) -> list: ...
def _pre_conditions(coins: list, n: int) -> None: ...
def change_making(coins: list, n: int) -> int: ...
def extended_change_making(coins: list, n: int) -> list: ...
