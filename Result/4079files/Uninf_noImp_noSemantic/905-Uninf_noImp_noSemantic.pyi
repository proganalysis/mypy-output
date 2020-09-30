from .apps import Applications
from .base import _ApiResourceBase
from .friends import Friends
from .groups import Groups
from .overlay import Overlay
from .screenshots import Screenshots
from .user import CurrentUser
from .utils import Utils
from typing import Any, Optional

class Api(_ApiResourceBase):
    utils: Utils = ...
    current_user: CurrentUser = ...
    friends: Friends = ...
    groups: Groups = ...
    apps: Applications = ...
    overlay: Overlay = ...
    screenshots: Screenshots = ...
    _app_id: Any = ...
    _lib: Any = ...
    _client: Any = ...
    def __init__(self, library_path: Any, app_id: Optional[Any] = ...) -> None: ...
    def init(self, app_id: Optional[Any] = ...) -> None: ...
    @classmethod
    def set_app_id(cls, app_id: Any) -> None: ...
    @property
    def app_id(self): ...
    @property
    def steam_running(self): ...
    @property
    def install_path(self): ...
    def start_app(self): ...
    def run_callbacks(self) -> None: ...
    def shutdown(self) -> None: ...
