from typing import Any, Dict, Optional

secret: str
User = str
logged_in_users: Dict[bytes, User]

def show_main_page(user: Optional[Any] = ...): ...
def check_credentials(): ...
def get_logged_in_user(): ...
def post_message(): ...
def show_search(): ...
def verify_user_exists(user: Any) -> None: ...
def show_user_page(user: Any): ...
def show_followers(user: Any): ...
def show_following(user: Any): ...
def fetch_static(filename: Any): ...
