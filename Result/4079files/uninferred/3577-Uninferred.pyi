from typing import Any

class StaircaseGenerator:
    __lower_bound: int = ...
    __upper_bound: int = ...
    __generated_numbers: Any = ...
    __legal: bool = ...
    __print_distance: int = ...
    __percentage: int = ...
    def __init__(self, lower_bound: int, upper_bound: int) -> None: ...
    def __check_bounds_for_range_restrictions(self) -> None: ...
    def generate_staircase_from_lower_to_upper_bound(self) -> None: ...
    @staticmethod
    def __check_single_number(number_to_check: Any): ...
    def reset_bounds(self, lower_bound: int, upper_bound: int) -> Any: ...
    def print_generated_numbers(self) -> None: ...
