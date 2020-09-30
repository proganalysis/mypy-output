from logging import Logger
from meta import CodeStyle, Ext, FromFmt, LongOpt, ToFmt
from os.path import abspath as abspath, isdir as isdir, realpath as realpath
from typing import Any, Dict, Iterable, List, Optional, Text

log: Logger

class PandocCmd:
    exts: Any = ...
    no_exts: Any = ...
    long_opts: Any = ...
    def __init__(self, input_file: Text, stylesheet: Text=..., javascript: Text=..., from_fmt: FromFmt=..., to_fmt: ToFmt=..., exts: List[Ext]=..., no_exts: List[Ext]=..., long_opts: Dict[LongOpt, Optional[Text]]=..., code_style: CodeStyle=..., mathjax_version: Text=..., mathjax_conf: Text=..., width: int=..., toc_depth: int=...) -> None: ...
    from_fmt: Any = ...
    def set_from_fmt(self, fmt: FromFmt) -> object: ...
    def set_opt(self, key: LongOpt, val: Optional[Text]=...) -> object: ...
    def set_opts(self, pairs: Dict[LongOpt, Optional[Text]]) -> object: ...
    to_fmt: Any = ...
    def set_to_fmt(self, fmt: ToFmt) -> object: ...
    input_file: Any = ...
    def set_input_file(self, file_path: Text) -> object: ...
    def set_width(self, n: int) -> object: ...
    def set_stylesheet(self, css_path: Text) -> object: ...
    javascript: Any = ...
    def set_javascript(self, js_path: Text) -> object: ...
    def set_toc_depth(self, n: int) -> object: ...
    def set_code_style(self, style: CodeStyle) -> object: ...
    def set_mathjax(self, version: Text, cfg: Text) -> object: ...
    def set_exts(self, exts: Iterable[Ext]) -> object: ...
    def set_ext(self, ext: Ext) -> object: ...
    def set_no_ext(self, ext: Ext) -> object: ...
    def set_no_exts(self, exts: Iterable[Ext]) -> object: ...
    @property
    def args(self) -> List[Text]: ...
    def before(self, text: Text) -> Text: ...
    def after(self, text: Text) -> Text: ...
    def execute(self) -> Text: ...
