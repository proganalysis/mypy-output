from typing import Dict

class StatusRequestData:
    repository: str = ...
    sha: str = ...
    state: str = ...
    description: str = ...
    url: str = ...
    context: str = ...
    @staticmethod
    def is_valid_status_data(data: Dict) -> bool: ...