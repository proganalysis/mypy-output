import logging
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QAction, QApplication
from typing import Any

PROBLEM_MSG_PRIMARY: str
PROBLEM_MSG_SECONDARY: str
_logger: logging.Logger

class ConfigWindow:
    about_dialog: Any = ...
    app: Any = ...
    action_create: Any = ...
    def __init__(self, app: QApplication) -> None: ...
    def _create_action_create(self) -> QAction: ...
    def _connect_all_file_menu_signals(self) -> None: ...
    def _connect_all_edit_menu_signals(self) -> None: ...
    def _connect_all_tools_menu_signals(self) -> None: ...
    def _connect_all_settings_menu_signals(self) -> None: ...
    def _connect_all_help_menu_signals(self): ...
    def _initialise_action_states(self) -> None: ...
    def _set_platform_specific_keyboard_shortcuts(self) -> None: ...
    def _none_action(self) -> None: ...
    def set_dirty(self) -> None: ...
    def closeEvent(self, event: QCloseEvent) -> Any: ...
    def config_modified(self) -> None: ...
    def is_dirty(self): ...
    def update_actions(self, items: Any, changed: Any) -> None: ...
    def set_undo_available(self, state: Any) -> None: ...
    def set_redo_available(self, state: Any) -> None: ...
    def save_completed(self, persist_global: Any) -> None: ...
    def cancel_record(self) -> None: ...
    def queryClose(self): ...
    def on_close(self) -> None: ...
    def on_quit(self) -> None: ...
    def on_insert_macro(self, macro: Any) -> None: ...
    def on_record(self) -> None: ...
    def _do_record(self, ok: bool, record_keyboard: bool, record_mouse: bool, delay: float) -> Any: ...
    def on_run_script(self) -> None: ...
    def _run_script(self) -> None: ...
    def on_advanced_settings(self) -> None: ...
    def on_show_log(self) -> None: ...
    @staticmethod
    def open_external_url(url: str) -> Any: ...
