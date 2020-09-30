from abc import ABCMeta, abstractmethod
from typing import Any, Optional

class AbstractDAO(metaclass=ABCMeta):
    @abstractmethod
    def load_songci_contents(self) -> Any: ...
    @abstractmethod
    def load_emblem_names(self) -> Any: ...
    @abstractmethod
    def save_emblems_field(self, emblem_with_field_list: Any, field_name: Any, index: Any) -> Any: ...

class MongoDAO(AbstractDAO):
    COLLECTION_EMBLEM: str = ...
    COLLECTION_SONGCI_CONTENT: str = ...
    logger: Any = ...
    data_source: Any = ...
    def load_songci_contents(self): ...
    def load_emblem_names(self): ...
    def random_emblem_name(self, where: Optional[Any] = ..., size: int = ...): ...
    def save_emblems_field(self, emblem_with_field_list: Any, field_name: Any, index: bool = ...) -> None: ...
    def _save_emblems_field(self, emblem_with_field_list: Any, field_name: Any) -> None: ...
