from scr.logic.components.component import Component as Cmp
from typing import Any

def update_saved_data_to_last_version(orig_data: Any, orig_version: Any): ...

class Theoretical(Cmp):
    def __init__(self, id_: Any, inlet_nodes_id: Any, outlet_nodes_id: Any, component_data: Any) -> None: ...
    def _eval_intrinsic_equations(self): ...