from gi.repository import Gtk
from typing import Any

class RecentSelector(Gtk.Grid):
    __gtype_name__: str = ...
    def open_recent(self, uri: str) -> None: ...
    recent_chooser: Any = ...
    search_entry: Any = ...
    open_button: Any = ...
    filter_text: str = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def custom_recent_filter_func(self, filter_info: Gtk.RecentFilterInfo) -> bool: ...
    def make_recent_filter(self) -> Gtk.RecentFilter: ...
    def on_filter_text_changed(self, *args: Any) -> None: ...
    def on_selection_changed(self, *args: Any) -> None: ...
    def on_activate(self, *args: Any) -> None: ...