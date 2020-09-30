import wb_ui_components
from typing import Any

class P4MainWindowComponents(wb_ui_components.WbMainWindowComponents):
    all_visible_table_columns: Any = ...
    def __init__(self, factory: Any) -> None: ...
    def setTopWindow(self, top_window: Any) -> None: ...
    def createProject(self, project: Any): ...
    def addProjectPreInitWizardHandler(self, name: Any, url: Any, wc_path: Any) -> None: ...
    def addProjectInitWizardHandler_Bg(self, wc_path: Any): ...
    def addProjectPostInitWizardHandler(self) -> None: ...
    def addProjectPreCloneWizardHandler(self, name: Any, url: Any, wc_path: Any) -> None: ...
    def addProjectCloneWizardHandler_Bg(self, name: Any, url: Any, wc_path: Any, scm_state: Any): ...
    def addProjectPostCloneWizardHandler(self) -> None: ...
    def about(self): ...
    debugLog: Any = ...
    def setupDebug(self) -> None: ...
    def setupMenuBar(self, mb: Any, addMenu: Any) -> None: ...
    def setupToolBarAtLeft(self, addToolBar: Any, addTool: Any) -> None: ...
    def setupToolBarAtRight(self, addToolBar: Any, addTool: Any) -> None: ...
    def setupTableContextMenu(self, m: Any, addMenu: Any) -> None: ...
    def setupTreeContextMenu(self, m: Any, addMenu: Any) -> None: ...