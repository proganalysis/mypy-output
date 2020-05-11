# (generated with --quick)

from typing import Any

Deserializer: Any
Serializer: Any
extract_config_property: Any

class IntegerDeserializer(Any):
    byte_order: Any
    signed: Any
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def configure(self, configs, is_key) -> None: ...
    def deserialize(self, topic, data) -> int: ...

class IntegerSerializer(Any):
    byte_order: Any
    int_size: int
    signed: Any
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def configure(self, configs, is_key) -> None: ...
    def serialize(self, topic, data) -> bytes: ...
