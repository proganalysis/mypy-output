import pkinter as pk
import tkinter as tk
from tkinter import ttk
from typing import Any, Optional

__title__: str
__author__: str
__version__: str

class NBTViewer(tk.Toplevel):
    parent: Any = ...
    file: Any = ...
    menu: Any = ...
    toolbar: Any = ...
    statusbar: Any = ...
    widget_paned_window: Any = ...
    widget_frame_tree: Any = ...
    widget_treeview: Any = ...
    scrollbar_horizontal: Any = ...
    scrollbar_vertical: Any = ...
    def __init__(self, parent: Any, *args: Any, **kwargs: Any) -> None: ...
    def load_nbt(self, file: str = ...) -> None: ...
    def load_nested(self, parent: Any, nbt_file: Any, tag: Any, compound_tag: Optional[Any] = ...) -> None: ...

class Tree(ttk.Treeview):
    parent: Any = ...
    def __init__(self, parent: Any, window: Any, **kwargs: Any) -> None: ...
    def refresh(self) -> None: ...

class Menu(tk.Menu):
    parent: Any = ...
    def __init__(self, parent: Any, *args: Any, **kwargs: Any) -> None: ...

class Toolbar(pk.Toolbar):
    parent: Any = ...
    def __init__(self, parent: Any, *args: Any) -> None: ...

class Statusbar(pk.Statusbar):
    status_variable: Any = ...
    def __init__(self, parent: Any, *args: Any) -> None: ...

def main() -> None: ...
