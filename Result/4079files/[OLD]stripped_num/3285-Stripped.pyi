# (generated with --quick)

from typing import Any

Utils: Any
logging: module

def add_user_to_preferences(chatid) -> None: ...
def get_user_link_preview_preference(chatid) -> bool: ...
def get_user_notifications_sound_preference(chatid) -> bool: ...
def remove_user_from_preferences(chatid) -> None: ...
def update_link_preview_preference(chatid, value) -> None: ...
def update_notifications_sound_preference(chatid, value) -> None: ...
def user_has_preferences(chatid) -> bool: ...
