from typing import Any

def create_jwt(project_id: Any, private_key_file: Any, algorithm: Any): ...
def error_str(rc: Any): ...
def on_connect(unused_client: Any, unused_userdata: Any, unused_flags: Any, rc: Any) -> None: ...
def on_disconnect(unused_client: Any, unused_userdata: Any, rc: Any) -> None: ...
def on_publish(unused_client: Any, unused_userdata: Any, unused_mid: Any) -> None: ...
def parse_command_line_args(): ...
def main() -> None: ...
