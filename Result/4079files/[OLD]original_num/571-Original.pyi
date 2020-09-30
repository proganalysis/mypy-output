# (generated with --quick)

from typing import Any

CorrectionController: Any
DioptasModel: Any
IntegrationWidget: Any
MagicMock: Any
QtTest: Any
QtWidgets: Any
click_button: Any
gc: module
mock: module
np: module
os: module
unittest_data_path: Any

class CorrectionControllerTest(Any):
    correction_controller: Any
    correction_widget: Any
    model: Any
    original_filename: str
    response_filename: str
    widget: Any
    def load_original_img(self) -> None: ...
    def load_response_img(self) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_changing_transfer_function_several_times(self) -> None: ...
    def test_correction_loaded(self) -> None: ...
    def test_disable_transfer_correction(self) -> None: ...
    def test_filenames_are_displayed_in_widget(self) -> None: ...
    def test_image_enable_and_disable(self) -> None: ...
    def test_image_enable_and_disable_with_calibration(self) -> None: ...
    def test_load_img_with_different_shape(self) -> None: ...
    def test_load_img_with_different_shape_and_calibration(self) -> None: ...
    def test_show_correction_in_img_widget_and_back(self) -> None: ...
    def test_transfer_correction_is_applied_correctly(self) -> None: ...