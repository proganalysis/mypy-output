from typing import Any, Optional

__all__: Any
DESC: Any
SCRIPT_CONFIG: Any
LOG: Any
DEFAULT_HEADERS: Any
ARTICLE_ID_SET: Any
ORDER_TOP: str
ORDER_COMMENT: str
ORDER_ADD: str
API_URL: str
BASE_URL: str
META: Any
HTML_PARSER_NAME: str

def main(i: Any, f: Optional[Any] = ..., start: int = ..., end: Any = ..., img: bool = ..., gif: bool = ..., email: bool = ..., **kw: Any) -> None: ...
def jianshu_zhuanti_main(zhuanti_list: Any, start: Any, end: Any, kw: Any) -> None: ...
def parser_list(task: Any): ...
def parser_content(task: Any): ...
def resulter_content(task: Any) -> None: ...
def parser_downloader_img(task: Any): ...
def resulter_downloader_img(task: Any) -> None: ...
