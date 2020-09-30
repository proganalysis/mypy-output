from typing import Any

class zynthian_gui_control_xy:
    canvas: Any = ...
    hline: Any = ...
    vline: Any = ...
    shown: bool = ...
    zyngui: Any = ...
    padx: int = ...
    width: Any = ...
    x: Any = ...
    x_zctrl: Any = ...
    xvalue_max: int = ...
    xvalue: int = ...
    pady: int = ...
    height: Any = ...
    y: Any = ...
    y_zctrl: Any = ...
    yvalue_max: int = ...
    yvalue: int = ...
    main_frame: Any = ...
    def __init__(self) -> None: ...
    def show(self) -> None: ...
    def hide(self) -> None: ...
    def set_controllers(self, x_zctrl: Any, y_zctrl: Any) -> None: ...
    def set_x_controller(self, x_zctrl: Any) -> None: ...
    def set_y_controller(self, y_zctrl: Any) -> None: ...
    def get_controller_values(self) -> None: ...
    def refresh(self) -> None: ...
    def cb_canvas(self, event: Any) -> None: ...
    def zyncoder_read(self) -> None: ...
    def refresh_loading(self) -> None: ...
    def switch_select(self, t: str = ...) -> None: ...
