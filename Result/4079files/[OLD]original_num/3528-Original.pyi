# (generated with --quick)

import datetime
import dateutil.tz.tz
from typing import Any, Type

CalendarEvent: Any
list_calendar_events: Any
os: module
parser: module
timedelta: Type[datetime.timedelta]
tzlocal: Type[dateutil.tz.tz.tzlocal]

class TestCalendarEvent:
    def test_str(self) -> None: ...

class TestListCalendarEvents:
    def test_all_day_events(self) -> None: ...
    def test_exclusions(self) -> None: ...
    def test_floating_time(self) -> None: ...
    def test_floating_time_other_dst(self) -> None: ...
    def test_longer_single_all_day_start_end_inclusive(self) -> None: ...
    def test_normal_events(self) -> None: ...
    def test_recurrence_different_dst(self) -> None: ...
    def test_recurring_all_day_exclusions(self) -> None: ...
    def test_recurring_all_day_exclusions_end(self) -> None: ...
    def test_recurring_all_day_start_end_inclusive(self) -> None: ...
    def test_recurring_all_day_start_in_between(self) -> None: ...
    def test_recurring_start_and_end_inclusive(self) -> None: ...
    def test_reucrring_change_dst(self) -> None: ...
    def test_reucrring_single_changes(self) -> None: ...
    def test_simple_recurring(self) -> None: ...
    def test_single_all_day_start_end_inclusive(self) -> None: ...
    def test_single_start_end_inclusive(self) -> None: ...
