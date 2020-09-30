# (generated with --quick)

from typing import Any
import unittest.case

MockMixin: Any
chrono: Any
functools: module
guisupport: Any
mock: module
tkinter: module
unittest: module

class CalendarPeriodConfig(Any, unittest.case.TestCase):
    def test_config_period_returned(self) -> None: ...
    def test_invalid_period_logs_and_raises_error(self) -> None: ...

class CalendarPeriodInternal(Any, unittest.case.TestCase):
    def test_internal_period_returned(self) -> None: ...

class CalendarPeriods(Any, unittest.case.TestCase):
    def test_calendar_periods_returned(self) -> None: ...

class ChangeMenuItemState(Any, unittest.case.TestCase):
    menu: Any
    def test_menu_item_disabled(self) -> None: ...
    def test_menu_item_enabled(self) -> None: ...

class CleanupIntStr(unittest.case.TestCase):
    def test_empty_string_returns_str_zero(self) -> None: ...
    def test_non_empty_string_returns_integer(self) -> None: ...

class EntryUpdateObserver(Any, unittest.case.TestCase):
    mock_widget: Any
    value: str
    def test_widget_delete_called(self) -> None: ...
    def test_widget_insert_called(self) -> None: ...

class FormatDate(Any, unittest.case.TestCase):
    date: Any
    mock_config: Any
    def test_date_formatted_with_default_format(self) -> None: ...
    def test_date_formatted_with_supplied_format(self) -> None: ...

class LabelUpdateObserver(Any, unittest.case.TestCase):
    mock_widget: Any
    value: str
    def test_widget_updated(self) -> None: ...

class TestAutoScrollBar(unittest.case.TestCase):
    scrollbar: Any
    def test_grid_called(self) -> None: ...
    def test_grid_remove_called(self) -> None: ...
    def test_pack_raises_exception(self) -> None: ...
    def test_place_raises_exception(self) -> None: ...
    def test_set_called(self) -> None: ...
    def test_str(self) -> None: ...

class WidgetEnableObserver(Any, unittest.case.TestCase):
    mock_ttk: Any
    mock_widget: Any
    def test_disable_calls_widget_state_and_widget_delete(self) -> None: ...
    def test_enable_calls_widget_state(self) -> None: ...