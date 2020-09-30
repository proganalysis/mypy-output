# (generated with --quick)

from typing import Any, Optional, Tuple

cv2: Any
numpy: module

class Canvas:
    BOTTOM_INFO_BAR_HEIGHT_MIN: int
    DONE_COUNT_TEXT_ROW: int
    FPS_TEXT_ROW: int
    INFERENCE_LABEL_TEXT_ROW: int
    LOADING_TEXT_ROW: int
    PAUSE_TEXT_ROW: int
    PRESS_ANY_KEY_ROW: int
    TEXT_FONT: Any
    TIMER_TEXT_ROW: int
    TOP_INFO_BAR_HEIGHT_MIN: int
    _bottom_bar_bottom: int
    _bottom_bar_height: int
    _bottom_bar_left: int
    _bottom_bar_right: int
    _bottom_bar_top: int
    _bottom_bar_width: int
    _canvas_height: int
    _canvas_image: Any
    _canvas_width: int
    _done_blue: int
    _done_count: int
    _done_green: int
    _done_red: int
    _draw_lines_large_to_grid: bool
    _gird_undone_image_transparency: float
    _grid_blue: int
    _grid_bottom: int
    _grid_green: int
    _grid_height: int
    _grid_image_list: list
    _grid_left: int
    _grid_line_thickness: int
    _grid_max_images: int
    _grid_max_images_str: str
    _grid_red: int
    _grid_right: int
    _grid_top: int
    _grid_width: int
    _image_done_rect_thickness: int
    _image_height: int
    _image_width: int
    _images_across: int
    _images_down: int
    _large_image_bottom: int
    _large_image_height: int
    _large_image_left: int
    _large_image_list: list
    _large_image_right: int
    _large_image_top: int
    _large_image_width: int
    _num_bar_top_text_rows: int
    _text_background_color: Tuple[int, int, int]
    _text_bg_height: Any
    _text_color: Tuple[int, int, int]
    _text_height: Any
    _text_scale: float
    _top_bar_bottom: int
    _top_bar_height: int
    _top_bar_left: int
    _top_bar_right: int
    _top_bar_text_left: int
    _top_bar_text_left_width: int
    _top_bar_text_row_tops: list
    _top_bar_text_top: int
    _top_bar_top: int
    _top_bar_width: int
    def __init__(self, canvas_width: int, canvas_height: int, images_down: int, images_across: int) -> None: ...
    def _draw_grid_image(self, image_index: int, transparency: float) -> None: ...
    def _draw_grid_lines(self) -> None: ...
    def _draw_large_image(self, image_index: int, transparency: float) -> None: ...
    def _draw_undone_images(self) -> None: ...
    def _get_image_square(self, image_index: int) -> Tuple[int, int, int, int]: ...
    def _get_top_bar_left_text_bg_rect(self, text_row: int) -> Tuple[int, Any, int, Any]: ...
    def _get_top_bar_left_text_leftmost(self) -> int: ...
    def _get_top_bar_right_text_bg_rect(self, text_row: int) -> Tuple[int, Any, int, Any]: ...
    def _get_top_bar_right_text_leftmost(self) -> int: ...
    def _put_text_on_canvas(self, text: str, text_left: int, text_top: int, text_min_width: int) -> None: ...
    def _put_text_top_bar_left(self, text: str, text_row: int = ...) -> None: ...
    def _put_text_top_bar_right(self, text: str, text_row: int = ...) -> None: ...
    def clear_loading(self) -> None: ...
    def clear_press_any_key(self) -> None: ...
    def clear_top_bar(self) -> None: ...
    def draw_done_count(self) -> None: ...
    def draw_inference_label(self, label_text: str) -> None: ...
    def get_canvas_image(self) -> Any: ...
    def hide_done_count(self) -> None: ...
    def hide_fps(self) -> None: ...
    def hide_timer(self) -> None: ...
    def load_images(self, image_list: list) -> None: ...
    def mark_image_done(self, image_index: int, label_text: Optional[str] = ...) -> None: ...
    def pause_start(self) -> None: ...
    def pause_stop(self) -> None: ...
    def press_any_key(self) -> None: ...
    def press_quit_key(self) -> None: ...
    def reset_canvas(self) -> None: ...
    def set_draw_lines(self, val: bool) -> None: ...
    def show_device(self, device: str) -> None: ...
    def show_fps(self, fps: float) -> None: ...
    def show_loading(self) -> None: ...
    def show_timer(self, time: float) -> None: ...
