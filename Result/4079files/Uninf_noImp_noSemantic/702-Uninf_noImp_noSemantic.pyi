from config import *
from typing import Any

def load_events_in_db(pj: dict, selectedSubjects: list, selectedObservations: list, selectedBehaviors: list, time_interval: str=...) -> Any: ...
def load_aggregated_events_in_db(pj: dict, selectedSubjects: list, selectedObservations: list, selectedBehaviors: list) -> Any: ...