from typing import Any

class Client:
    _bus: Any = ...
    _main_loop: Any = ...
    _request_path: Any = ...
    _response: Any = ...
    _results: Any = ...
    _portal: Any = ...
    def __init__(self, bus: Any, main_loop: Any) -> None: ...
    def _response_cb(self, response: Any, results: Any, object_path: Any) -> None: ...
    def run(self, args: Any): ...
    def cmd_open_file(self): ...
    def cmd_save_file(self, content: Any): ...
    def cmd_open_uri(self, uri: Any): ...
    def cmd_launch_file(self, filename: Any): ...
    def cmd_screenshot(self): ...

def main(argv: Any): ...