# (generated with --quick)

from typing import Any, List
import unittest.case

GNUCashBook: Any
MARKER_XIRR_FALSE: str
MARKER_XIRR_TRUE: str
TestInfo: Any
cols: Any
decimal: module
is_datetime64_any_dtype: Any
piecash: Any
unittest: module

class GnuCashBook_Test(unittest.case.TestCase):
    __doc__: str
    account_fields: list
    comm_fields: List[str]
    price_fields: List[str]
    split_fields: List[str]
    tr_fields: list
    def dataframe_fields_control(self, df, etalon_fields, df_name) -> None: ...
    def df_notempty(self, df, name_df) -> None: ...
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_account_fullname(self) -> None: ...
    def test_account_values(self) -> None: ...
    def test_accounts_count(self) -> None: ...
    def test_accounts_index(self) -> None: ...
    def test_accounts_notempty(self) -> None: ...
    def test_commodities_index(self) -> None: ...
    def test_fields(self) -> None: ...
    def test_prices_value_decimal(self) -> None: ...
    def test_rootaccount(self) -> None: ...
    def test_splits_count(self) -> None: ...
    def test_splits_index(self) -> None: ...
    def test_splits_notempty(self) -> None: ...
    def test_splits_quantity_decimal(self) -> None: ...
    def test_splits_value_decimal(self) -> None: ...
    def test_transaction_dates(self) -> None: ...
    def test_transactions_count(self) -> None: ...
    def test_transactions_index(self) -> None: ...
