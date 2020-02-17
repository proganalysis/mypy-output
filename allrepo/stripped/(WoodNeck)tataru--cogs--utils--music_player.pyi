# (generated with --quick)

from typing import Any, Coroutine

MusicQueue: Any
MusicType: Any
asyncio: module
discord: Any
os: module
subprocess: module
time: module

class MusicPlayer:
    channel: Any
    cog: Any
    currentSong: Any
    loop: bool
    player: Any
    queue: Any
    server: Any
    voiceClient: Any
    def __init__(self, cog, voiceClient, server, channel) -> None: ...
    def add(self, song) -> None: ...
    def afterPlay(self) -> None: ...
    def displayCurrentStatus(self, channel) -> Coroutine[Any, Any, None]: ...
    def makeLocalPlayer(self, fileDir) -> None: ...
    def makeYoutubePlayer(self, url) -> Coroutine[Any, Any, None]: ...
    def parseTime(self, time) -> str: ...
    def play(self) -> Coroutine[Any, Any, None]: ...
    def printSongList(self, channel) -> Coroutine[Any, Any, None]: ...
    def shouldPlay(self) -> bool: ...
    def skip(self) -> Coroutine[Any, Any, None]: ...
    def skipIndex(self, ctx, index) -> Coroutine[Any, Any, None]: ...
    def stop(self) -> None: ...
