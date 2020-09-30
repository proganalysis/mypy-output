from typing import Any

def gen_routing_key(device: Any, platform: Any, arch: Any) -> str: ...
def print_usage() -> None: ...

class BuildRpcServer:
    EXCHANGE: str = ...
    EXCHANGE_TYPE: str = ...
    connection_: Any = ...
    channel_: Any = ...
    closing_: bool = ...
    consumer_tag_: Any = ...
    device_: Any = ...
    platform_: Any = ...
    arch_: Any = ...
    routing_key_: Any = ...
    def __init__(self, device: Any, platform: Any, arch: Any) -> None: ...
    def connect(self): ...
    def reconnect(self) -> None: ...
    def on_connection_open(self, unused_connection: Any) -> None: ...
    def add_on_connection_close_callback(self) -> None: ...
    def open_channel(self) -> None: ...
    def on_channel_open(self, channel: Any) -> None: ...
    def add_on_channel_close_callback(self) -> None: ...
    def setup_exchange(self, exchange_name: Any) -> None: ...
    def on_exchange_declareok(self, unused_frame: Any) -> None: ...
    def setup_queue(self, queue_name: Any) -> None: ...
    def on_queue_declareok(self, method_frame: Any) -> None: ...
    def on_bindok(self, unused_frame: Any) -> None: ...
    def start_consuming(self) -> None: ...
    def on_consumer_cancelled(self, method_frame: Any) -> None: ...
    def add_on_cancel_callback(self) -> None: ...
    def on_channel_closed(self, channel: Any, reply_code: Any, reply_text: Any) -> None: ...
    def on_connection_closed(self, connection: Any, reply_code: Any, reply_text: Any) -> None: ...
    def run(self) -> None: ...
    def build_package(self, op_id: Any, branding_options: Any, package_types: Any, destination: Any, routing_key: Any): ...
    def send_status(self, routing_key: Any, op_id: Any, progress: Any, status: Any) -> None: ...
    def send_response(self, routing_key: Any, op_id: Any, body: Any) -> None: ...
    def on_request(self, ch: Any, method: Any, props: Any, body: Any) -> None: ...
    def acknowledge_message(self, delivery_tag: Any) -> None: ...
