from setuptools.command.build_ext import build_ext
from typing import Any

def read(*names: Any, **kwargs: Any): ...

class optional_build_ext(build_ext):
    extensions: Any = ...
    def run(self) -> None: ...
    def _unavailable(self, e: Any) -> None: ...
