from typing import Any, Optional

producer: Any
logger: Any

def tick_to_kafka(security_item: Optional[Any] = ...) -> None: ...
def _tick_to_kafka(security_item: Any) -> None: ...
def kdata_to_kafka(security_item: Optional[Any] = ..., fuquan: str = ...) -> None: ...
def _kdata_to_kafka(security_item: Any, fuquan: str = ...) -> None: ...
def delete_topic(topic: Any) -> None: ...
def list_topics(): ...
def delete_all_topics() -> None: ...
def cryptocurrency_tick_to_kafka(exchange: Any, pairs: Optional[Any] = ...) -> None: ...
