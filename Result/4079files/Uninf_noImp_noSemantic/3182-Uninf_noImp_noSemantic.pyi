from typing import Any

def test_compose_message() -> None: ...
def test_correct_serialization(nsproxy: Any, agent_serial: Any, socket_serial: Any, result: Any) -> None: ...
def test_serialize_message() -> None: ...
def test_deserialize_message() -> None: ...
def test_reqrep(nsproxy: Any, serializer: Any, message: Any, response: Any): ...
def test_reqrep_raw_zmq_outside(nsproxy: Any) -> None: ...
def test_pushpull(nsproxy: Any, serializer: Any, message: Any) -> None: ...
def test_pushpull_raw_zmq_outside(nsproxy: Any) -> None: ...
def test_pubsub(nsproxy: Any, serializer: Any, message: Any) -> None: ...
def test_pubsub_raw_zmq_outside(nsproxy: Any) -> None: ...
