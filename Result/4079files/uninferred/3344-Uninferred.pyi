from json import dumps as dumps
from sys import version as version
from typing import Any

class HaveIBeenPwndDradis:
    arg: Any = ...
    verifyCert: bool = ...
    dradisApiToken: Any = ...
    dradisProjectId: Any = ...
    dradisUrl: Any = ...
    dradisDebug: bool = ...
    dradisSession: Any = ...
    querySession: Any = ...
    def __init__(self) -> None: ...
    def run(self) -> None: ...
    def searchApi(self, query: str) -> Any: ...
    def performQuery(self, userEmailOrDomain: str, projectId: str) -> Any: ...
    def createIssue(self, userEmailOrDomain: Any, projectId: Any, nodeId: Any): ...
    def createNode(self, nodeName: str, projectId: int) -> Any: ...
    def createEvidence(self, nodeId: Any, projectId: Any, issueId: Any, evidenceData: Any): ...
    def processArguments(self): ...
