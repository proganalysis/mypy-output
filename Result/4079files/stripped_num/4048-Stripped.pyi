# (generated with --quick)

from typing import Any, Optional

MP4: Any
MP4StreamInfoError: Any
os: module
re: module
string: module
subprocess: module

def correct_date_format(date) -> Optional[bool]: ...
def process_image(filename, user, date = ..., caption = ..., tags = ..., code = ...) -> None: ...
def process_video(filename, user, date = ..., caption = ..., tags = ..., code = ...) -> None: ...
def remove_unicode(caption) -> Any: ...
def xml_tags(user) -> bytes: ...
