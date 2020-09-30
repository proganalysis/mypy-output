from threading import Thread
from typing import Any

class ValidationWorker(Thread):
    check_pool: Any = ...
    current_object: Any = ...
    id: Any = ...
    queue: Any = ...
    result: Any = ...
    seen_list: Any = ...
    def __init__(self, id: Any, queue: Any, seen_list: Any, check_pool: Any, result: Any) -> None: ...
    def run(self) -> None: ...
    def is_seen_object(self): ...
    def validate_object(self): ...
    def save_validation_results(self, validation_results: Any) -> None: ...
    def save_failed_object(self) -> None: ...
