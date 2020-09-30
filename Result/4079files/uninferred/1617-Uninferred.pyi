from .blockchainobject import BlockchainObject, BlockchainObjects
from .instance import AbstractBlockchainInstanceProvider
from typing import Any

log: Any

class Proposal(BlockchainObject, AbstractBlockchainInstanceProvider):
    def __init__(self, data: Any, *args: Any, **kwargs: Any) -> None: ...
    def refresh(self) -> None: ...
    @property
    def proposed_operations(self) -> None: ...
    @property
    def proposer(self): ...
    @property
    def expiration(self): ...
    @property
    def review_period(self): ...
    @property
    def is_in_review(self): ...

class Proposals(BlockchainObjects, AbstractBlockchainInstanceProvider):
    identifier: Any = ...
    def __init__(self, account: Any, *args: Any, **kwargs: Any) -> None: ...
    def refresh(self, *args: Any, **kwargs: Any) -> None: ...
