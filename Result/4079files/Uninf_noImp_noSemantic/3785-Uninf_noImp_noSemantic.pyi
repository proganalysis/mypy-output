from builtins import *
from typing import Any
from ycmd.completers.completer import Completer

class PythonCompleter(Completer):
    _jedi_lock: Any = ...
    _settings_for_file: Any = ...
    _environment_for_file: Any = ...
    _environment_for_interpreter_path: Any = ...
    _sys_path_for_file: Any = ...
    def __init__(self, user_options: Any) -> None: ...
    def SupportedFiletypes(self): ...
    def OnFileReadyToParse(self, request_data: Any) -> None: ...
    def _SettingsForRequest(self, request_data: Any): ...
    def _GetSettings(self, module: Any, filepath: Any, client_data: Any): ...
    def _EnvironmentForInterpreterPath(self, interpreter_path: Any): ...
    def _EnvironmentForRequest(self, request_data: Any): ...
    def _GetSysPath(self, request_data: Any, environment: Any): ...
    def _SysPathForFile(self, request_data: Any, environment: Any): ...
    def _GetJediScript(self, request_data: Any): ...
    def _GetJediScriptForDefinition(self, request_data: Any, definition: Any): ...
    def _GetExtraData(self, completion: Any): ...
    def ComputeCandidatesInner(self, request_data: Any): ...
    def DetailCandidates(self, request_data: Any, candidates: Any): ...
    def GetSubcommandsMap(self): ...
    def _BuildGoToResponse(self, definitions: Any): ...
    def _GoToDefinition(self, request_data: Any): ...
    def _GoToType(self, request_data: Any): ...
    def _GoToReferences(self, request_data: Any): ...
    def _BuildTypeInfo(self, definition: Any): ...
    def _GetType(self, request_data: Any): ...
    def _GetDoc(self, request_data: Any): ...
    def DebugInfo(self, request_data: Any): ...
