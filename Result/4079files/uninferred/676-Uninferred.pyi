import abc
from .User import User as User
from abc import ABC, abstractmethod
from typing import Any, List

class UserSource(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def get_user_by_identifier(self, identifier: int) -> User: ...
    def get_all_users(self) -> List[User]: ...
    def add_user(self, user: User) -> Any: ...