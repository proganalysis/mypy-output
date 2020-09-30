# (generated with --quick)

from typing import Any, Optional

logger: logging.Logger
logging: module
subprocess: module
utils: Any

class RRDServer(object):
    _rrd: Optional[subprocess.Popen[bytes]]
    def _require_rrd(self) -> Any: ...
    def send_command(self, cmdbytes) -> None: ...
    def update_ds_with_timestamp(self, rrdfile, ds_name, timestamp, value) -> None: ...
    def update_with_timestamps(self, rrdfile, data) -> None: ...

class RRDToolError(Exception): ...

class UnknownRRDToolResponse(RRDToolError): ...