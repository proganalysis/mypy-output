from base import ScrollArea
from typing import Any, Optional

__author__: str

class DownloadFrame(ScrollArea):
    parent: Any = ...
    mainLayout: Any = ...
    def __init__(self, parent: Optional[Any] = ...) -> None: ...
    spaceLine: Any = ...
    currentStorageFolderLabel: Any = ...
    currentStorageFolder: Any = ...
    selectButton: Any = ...
    topShowLayout: Any = ...
    def setHeader(self) -> None: ...
    singsTable: Any = ...
    def setMusicTable(self) -> None: ...
