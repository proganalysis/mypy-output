from PyQt5.QtWidgets import QAbstractItemView as QAbstractItemView, QWidget
from typing import Any

class AbstractWindow(QWidget):
    def __init__(self) -> None: ...

class MainWindow(AbstractWindow):
    accounting_window: Any = ...
    items_model: Any = ...
    cart_model: Any = ...
    def __init__(self, items: Any, cart: Any) -> None: ...
    def init_ui(self) -> None: ...
    def on_click(self) -> None: ...

class AccountingWindow(AbstractWindow):
    title: str = ...
    left: int = ...
    top: int = ...
    width: int = ...
    height: int = ...
    items_model: Any = ...
    cart_model: Any = ...
    def __init__(self, items: Any, cart: Any) -> None: ...
    wrapper: Any = ...
    item_request_wrapper: Any = ...
    customer_id_label: Any = ...
    customer_id_input: Any = ...
    item_request_id_label: Any = ...
    item_request_id_input: Any = ...
    item_request_id_search: Any = ...
    right: Any = ...
    def init_ui(self) -> None: ...
    def put_item_in_cart(self) -> None: ...

def main(items: Any, cart: Any) -> None: ...
