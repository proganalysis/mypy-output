# (generated with --quick)

from typing import Any, Tuple

GObject: Any
Gtk: Any
log: logging.Logger
logging: module
re: module

def append_element(path, selector) -> None: ...
def create_context_for_path(path, parent) -> Any: ...
def draw_style_common(context, cr, x, y, width, height) -> Tuple[Any, Any, Any, Any]: ...
def get_style(parent, selector) -> Any: ...
def query_size(context, width, height) -> Tuple[Any, Any]: ...
