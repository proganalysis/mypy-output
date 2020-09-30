import pandas as pd
from typing import Any

class OuterModel:
    __crossloadings: Any = ...
    __outer_model: Any = ...
    def __init__(self, data: pd.DataFrame, scores: pd.DataFrame, weights: pd.DataFrame, odm: pd.DataFrame, r_squared: pd.Series): ...
    def model(self) -> pd.DataFrame: ...
    def crossloadings(self) -> pd.DataFrame: ...
