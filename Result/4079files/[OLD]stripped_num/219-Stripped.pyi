# (generated with --quick)

from typing import Any, Generator

signals: Any

class TutorialSpiderMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler) -> Any: ...
    def process_spider_exception(response: TutorialSpiderMiddleware, exception, spider) -> None: ...
    def process_spider_input(response: TutorialSpiderMiddleware, spider) -> None: ...
    def process_spider_output(response: TutorialSpiderMiddleware, result, spider) -> Generator[Any, Any, None]: ...
    def process_start_requests(start_requests: TutorialSpiderMiddleware, spider) -> Generator[Any, Any, None]: ...
    def spider_opened(self, spider) -> None: ...