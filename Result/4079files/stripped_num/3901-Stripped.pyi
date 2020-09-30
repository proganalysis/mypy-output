# (generated with --quick)

from typing import Any

Deserializer: Any
Serializer: Any
extract_config_property: Any

class StringDeserializer(Any):
    encoding: Any
    on_error: Any
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def configure(self, configs, is_key) -> None: ...
    def deserialize(self, topic, data) -> Any: ...

class StringSerializer(Any):
    encoding: Any
    on_error: Any
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def configure(self, configs, is_key) -> None: ...
    def serialize(self, topic, data) -> bytes: ...
