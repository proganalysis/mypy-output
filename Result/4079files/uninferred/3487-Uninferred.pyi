from .methods import Method as Method, Methods as Methods
from .request import Request as Request
from .response import Response as Response
from typing import Any, Iterable, Optional, Union

async def call(method: Method, *args: Any, **kwargs: Any) -> Any: ...
async def safe_call(request: Request, methods: Methods, debug: bool) -> Response: ...
async def call_requests(requests: Union[Request, Iterable[Request]], methods: Methods, debug: bool) -> Response: ...
async def dispatch_pure(request: str, methods: Methods, context: Any, convert_camel_case: bool, debug: bool) -> Response: ...
async def dispatch(request: str, methods: Optional[Methods]=..., *, basic_logging: bool=..., convert_camel_case: bool=..., context: Any=..., debug: bool=..., trim_log_values: bool=..., **kwargs: Any) -> Response: ...
