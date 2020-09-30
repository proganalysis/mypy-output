# (generated with --quick)

from typing import Any, Callable, Dict, List, Optional, Tuple, Union

TEXCOUNT_PATH: str
lettersR: str
os: module
re: module
subprocess: module
wordsR: str

def copyFolderStructure(src: str, target: str) -> None: ...
def correctLetters(letters: dict, words: dict) -> None: ...
def count(path: str, buildPath: str, fileName: str) -> Tuple[bool, Union[dict, str]]: ...
def doCompile(proj: str, buildPath: str, cfg: dict, log: Callable[[str], None]) -> bool: ...
def getProjPath(proj: str) -> str: ...
def parseOutput(data: str, regex: str) -> Dict[str, Any]: ...
def runSubprocess(cmd: List[str], out: Callable[[str], None], cwd: Optional[str] = ..., env: Dict[str, str] = ...) -> int: ...