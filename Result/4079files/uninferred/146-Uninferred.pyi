from typing import Any
from zdict.dictionary import DictBase
from zdict.models import Record

class MoeDict(DictBase):
    API: str = ...
    @property
    def provider(self): ...
    @property
    def title(self): ...
    def _get_url(self, word: Any) -> str: ...
    def show(self, record: Record) -> Any: ...
    def query(self, word: str) -> Any: ...

def is_other_format(char: Any): ...
def remove_cf(data: Any): ...
def clean(data: Any, clean_cf: bool = ...): ...

class MoeDictTaiwanese(DictBase):
    API: str = ...
    @property
    def provider(self): ...
    @property
    def title(self): ...
    def _get_url(self, word: Any) -> str: ...
    def show(self, record: Record) -> Any: ...
    def query(self, word: str) -> Any: ...