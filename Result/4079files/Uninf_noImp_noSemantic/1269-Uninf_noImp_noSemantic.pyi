from collections import namedtuple
from decimal import Decimal
from typing import Any, Optional, Tuple

Installment = namedtuple('Installment', 'number payment interest principal total_interest balance')

class Loan:
    principal: Any = ...
    interest: Any = ...
    term: Any = ...
    term_unit: Any = ...
    compounded: Any = ...
    n_periods: Any = ...
    _schedule: Any = ...
    _currency: Any = ...
    def __init__(self, principal: Any, interest: Any, term: Any, term_unit: str = ..., compounded: str = ..., currency: str = ...) -> None: ...
    def __repr__(self): ...
    @staticmethod
    def _quantize(value: Any): ...
    def schedule(self, nth_payment: Optional[Any] = ...): ...
    @property
    def _monthly_payment(self): ...
    @property
    def monthly_payment(self): ...
    def _simple_interest(self, term: Any): ...
    @property
    def apr(self) -> Decimal: ...
    @property
    def apy(self) -> Decimal: ...
    @property
    def total_principal(self) -> Decimal: ...
    @property
    def total_interest(self) -> Decimal: ...
    @property
    def total_paid(self) -> Decimal: ...
    @property
    def interest_to_principle(self) -> float: ...
    @property
    def years_to_pay(self) -> float: ...
    @property
    def summarize(self) -> None: ...
    def split_payment(self, number: int, amount: Decimal) -> Tuple[Decimal, Decimal]: ...
    def _amortize(self): ...
