from typing import Any

def setup_function(function: Any) -> None: ...
def plugin(mocker: Any): ...
def session(): ...
def test_should_update_icon_when_timer_changes(plugin: Any) -> None: ...
def test_should_show_widget_when_session_starts(plugin: Any) -> None: ...
def test_should_hide_widget_when_session_ends(plugin: Any) -> None: ...

class TestActivePlugin:
    def setup_method(self, method: Any) -> None: ...
    def test_should_register_tray_icon_provider(self, plugin: Any) -> None: ...
    def test_should_show_menu_when_session_is_running(self, session: Any, plugin: Any) -> None: ...
    def test_should_hide_menu_when_session_is_not_running(self, session: Any, plugin: Any) -> None: ...
    def test_should_connect_menu_events(self, connect_events: Any, plugin: Any) -> None: ...

class TestDeactivatePlugin:
    def setup_method(self, method: Any) -> None: ...
    def test_should_unregister_tray_icon_provider(self, plugin: Any) -> None: ...
    def test_should_hide_widget_when_plugin_deactivate(self, plugin: Any) -> None: ...
    def test_should_disconnect_menu_events_when_plugin_deactivate(self, disconnect_events: Any, plugin: Any) -> None: ...

def test_should_call_menu_pop(plugin: Any) -> None: ...
