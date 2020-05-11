# (generated with --quick)

from typing import Any, BinaryIO, Dict, Iterable, List, Optional, Type, TypeVar, Union

Stats = Dict[str, Union[int, str]]

Body: Type[Union[bytes, str]]
DEFAULT_DELAY: int
DEFAULT_PRIORITY: int
DEFAULT_TTR: int
DEFAULT_TUBE: str
ERROR_RESPONSES: Dict[bytes, type]
JobOrID: Type[Union[Job, int]]
__version__: str
socket: module

_TClient = TypeVar('_TClient', bound=Client)

class BadFormatError(BeanstalkdError):
    __doc__: str

class BeanstalkdError(Error):
    __doc__: str

class BuriedError(BeanstalkdError):
    __doc__: str
    id: Optional[int]
    def __init__(self, values: Optional[List[bytes]] = ...) -> None: ...

class Client:
    __doc__: str
    _reader: BinaryIO
    _sock: socket.socket
    encoding: Any
    def __enter__(self: _TClient) -> _TClient: ...
    def __exit__(self, *args) -> None: ...
    def __init__(self, host: str = ..., port: int = ..., encoding: Optional[str] = ..., use: str = ..., watch: Union[str, Iterable[str]] = ...) -> None: ...
    def _int_cmd(self, cmd: bytes, expected: bytes) -> int: ...
    def _job_cmd(self, cmd: bytes, expected: bytes) -> Job: ...
    def _list_cmd(self, cmd: bytes) -> List[str]: ...
    def _peek_cmd(self, cmd: bytes) -> Job: ...
    def _read_chunk(self, size: int) -> bytes: ...
    def _send_cmd(self, cmd: bytes, expected: bytes) -> List[bytes]: ...
    def _stats_cmd(self, cmd: bytes) -> Dict[str, Union[int, str]]: ...
    def bury(self, job: Job, priority: int = ...) -> None: ...
    def close(self) -> None: ...
    def delete(self, job: Union[Job, int]) -> None: ...
    def ignore(self, tube: str) -> int: ...
    def kick(self, bound: int) -> int: ...
    def kick_job(self, job: Union[Job, int]) -> None: ...
    def pause_tube(self, tube: str, delay: int) -> None: ...
    def peek(self, id: int) -> Job: ...
    def peek_buried(self) -> Job: ...
    def peek_delayed(self) -> Job: ...
    def peek_ready(self) -> Job: ...
    def put(self, body: Union[bytes, str], priority: int = ..., delay: int = ..., ttr: int = ...) -> int: ...
    def release(self, job: Job, priority: int = ..., delay: int = ...) -> None: ...
    def reserve(self, timeout: Optional[int] = ...) -> Job: ...
    def stats(self) -> Dict[str, Union[int, str]]: ...
    def stats_job(self, job: Union[Job, int]) -> Dict[str, Union[int, str]]: ...
    def stats_tube(self, tube: str) -> Dict[str, Union[int, str]]: ...
    def touch(self, job: Job) -> None: ...
    def tubes(self) -> List[str]: ...
    def use(self, tube: str) -> None: ...
    def using(self) -> str: ...
    def watch(self, tube: str) -> int: ...
    def watching(self) -> List[str]: ...

class DeadlineSoonError(BeanstalkdError):
    __doc__: str

class DrainingError(BeanstalkdError):
    __doc__: str

class Error(Exception):
    __doc__: str

class ExpectedCrlfError(BeanstalkdError):
    __doc__: str

class InternalError(BeanstalkdError):
    __doc__: str

class Job:
    __slots__ = ["body", "id"]
    __doc__: str
    body: Union[bytes, str]
    id: int
    def __init__(self, id: int, body: Union[bytes, str]) -> None: ...

class JobTooBigError(BeanstalkdError):
    __doc__: str

class NotFoundError(BeanstalkdError):
    __doc__: str

class NotIgnoredError(BeanstalkdError):
    __doc__: str

class OutOfMemoryError(BeanstalkdError):
    __doc__: str

class TimedOutError(BeanstalkdError):
    __doc__: str

class UnknownCommandError(BeanstalkdError):
    __doc__: str

class UnknownResponseError(Error):
    __doc__: str
    status: bytes
    values: List[bytes]
    def __init__(self, status: bytes, values: List[bytes]) -> None: ...

def _parse_chunk(data: bytes, size: int) -> bytes: ...
def _parse_response(line: bytes, expected: bytes) -> List[bytes]: ...
def _parse_simple_yaml(buf: bytes) -> Dict[str, Union[int, str]]: ...
def _parse_simple_yaml_list(buf: bytes) -> List[str]: ...
def _to_id(j: Union[Job, int]) -> int: ...
