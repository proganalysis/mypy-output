from enum import Enum
from typing import Any

class LobbyState(Enum):
    WaitingForHost: int = ...
    WaitingForGameCreation: int = ...
    InGame: int = ...

CAH_lobby_server: Any
socketio: Any

def test_message(message: Any) -> None: ...
def client_connected(data: Any) -> None: ...
def test_disconnect() -> None: ...
def with_session(func: Any): ...
def login(): ...
def add_player(): ...
def index(): ...
def user(): ...
def czar(): ...
def lobby_state(): ...
def player_count(): ...
def hand(): ...
def judgement(): ...
def submit_white_card(data: Any): ...
def host(): ...
def address(): ...
def play(): ...
def interrupt(): ...
def shutdown_server() -> None: ...
def shutdown(): ...
