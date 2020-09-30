# (generated with --quick)

from typing import Any, Dict, List, Tuple

opt: Any
os: module

class TestSuiteWalletConv(Any, Any):
    __doc__: str
    cmd_group: Tuple[Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str]]
    networks: Tuple[str]
    sources: Dict[str, Dict[str, str]]
    tmpdir_nums: List[int]
    def __init__(self, trunner, cfgs, spawn) -> Any: ...
    def ref_bip39_conv(self) -> Any: ...
    def ref_bip39_conv_out(self) -> Any: ...
    def ref_brain_conv(self) -> Any: ...
    def ref_hex_conv(self) -> Any: ...
    def ref_hex_conv_out(self) -> Any: ...
    def ref_hincog_blkdev_conv_out(self) -> str: ...
    def ref_hincog_conv(self, wfk = ..., add_uopts = ...) -> Any: ...
    def ref_hincog_conv_old(self) -> Any: ...
    def ref_hincog_conv_out(self, ic_f = ...) -> Any: ...
    def ref_incog_conv(self, wfk = ..., in_fmt = ..., desc = ...) -> Any: ...
    def ref_incog_conv_out(self) -> Any: ...
    def ref_incox_conv(self) -> Any: ...
    def ref_incox_conv_out(self) -> Any: ...
    def ref_mn_conv(self, ext = ..., desc = ...) -> Any: ...
    def ref_mn_conv_out(self) -> Any: ...
    def ref_seed_conv(self) -> Any: ...
    def ref_seed_conv_out(self) -> Any: ...
    def ref_wallet_conv(self) -> Any: ...
    def ref_wallet_conv_out(self) -> Any: ...
    def walletconv_in(self, infile, desc, uopts = ..., pw = ..., oo = ...) -> Any: ...
    def walletconv_out(self, desc, out_fmt = ..., uopts = ..., uopts_chk = ..., pw = ...) -> Any: ...

def __getattr__(name) -> Any: ...
