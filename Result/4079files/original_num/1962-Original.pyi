# (generated with --quick)

import requests.adapters
import requests.models
import requests.packages.urllib3.util.retry
import requests.sessions
from typing import Any, Dict, Type

HTTPAdapter: Type[requests.adapters.HTTPAdapter]
Retry: Type[requests.packages.urllib3.util.retry.Retry]
datetime: Type[datetime.datetime]
logging: module
os: module
requests: module
xml: Any

class instagram:
    csrftoken: Any
    headers: Dict[str, str]
    mid: Any
    session: requests.sessions.Session
    sessionid: Any
    userid: Any
    def __init__(self, cookie) -> None: ...
    def close(self) -> None: ...
    def downloadReel(self, resp) -> None: ...
    def downloadStoryLive(self, resp) -> None: ...
    def downloadTray(self, resp) -> None: ...
    def formatPath(self, user: str, pk: int, timestamp: int, postid: str, mediatype: int) -> str: ...
    def getFile(self, url: str, dest: str) -> None: ...
    def getReelMedia(self, user) -> requests.models.Response: ...
    def getReelTray(self) -> requests.models.Response: ...
    def getStories(self) -> requests.models.Response: ...
    def getUserIDs(self, json: dict) -> list: ...
    def getUserStories(self, user) -> requests.models.Response: ...
