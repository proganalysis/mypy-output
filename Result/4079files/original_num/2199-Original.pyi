# (generated with --quick)

import queue
import threading
from typing import Any, Optional, Type, TypeVar

Queue: Type[queue.Queue]
Thread: Type[threading.Thread]
errno: module
os: module
progressbar: Any
re: module
requests: module
time: module

AnyStr = TypeVar('AnyStr', str, bytes)

class Aria2JsonRpc(object):
    __doc__: str
    rpc_url: Any
    def __init__(self, rpc_url = ...) -> None: ...
    def addUris(self, urls, dir = ..., out = ...) -> None: ...
    def execuetJsonRpcCmd(self, method, param = ...) -> Optional[str]: ...
    def isAlive(self) -> bool: ...

class DownloadQueue(threading.Thread):
    daemon: bool
    queue: Any
    def __init__(self, queue) -> None: ...
    def run(self) -> Any: ...

def aira2_download(download_list) -> None: ...
def clean_filename(string: str) -> str: ...
def direct_download(session, url: str, file: str, resume = ..., retry = ...) -> None: ...
def download_queue(session, download_list, queue_length = ...) -> None: ...
def generate_path(path_list: list) -> str: ...
def link_check(hostname: str, href: str) -> str: ...
def mkdir_p(path, mode = ...) -> None: ...
def raw_unicode_escape(string: str) -> str: ...
def unescape(s: AnyStr) -> AnyStr: ...
def unquote(string: str, encoding: str = ..., errors: str = ...) -> str: ...
