# (generated with --quick)

from typing import Any, Coroutine

BeautifulSoup: Any
HTTPHandler: Any
Page: Any
Session: Any
commands: Any
discord: Any

class NSFW:
    bot: Any
    히토미: Any
    def __init__(self, bot) -> None: ...
    def alertOnlyInNSFW(self, channel) -> Coroutine[Any, Any, None]: ...
    def getAllMetaInfo(self, meta) -> Any: ...
    def getMetaInfo(self, meta) -> Any: ...
    def isNSFW(self, channel) -> Any: ...
    def readHitomi(self, cmdMsg, index, images, em) -> Coroutine[Any, Any, None]: ...

def setup(bot) -> None: ...
