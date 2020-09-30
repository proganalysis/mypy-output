from nougat.exceptions import *
from nougat import Nougat as Nougat
from nougat.context import Request as Request, Response as Response
from typing import Any

class TestMiddleware:
    async def test_no_middleware(self, app: Nougat, port: int) -> Any: ...
    async def test_middleware_with_no_param(self, app: Nougat, port: int) -> Any: ...
    async def test_middleware_with_all_params(self, app: Nougat, port: int) -> Any: ...
    async def test_middleware_with_part_of_params(self, app: Nougat, port: int) -> Any: ...
    async def test_middleware_chain(self, app: Nougat, port: int) -> Any: ...
    async def test_middleware_chain_stop_at_one_step(self, app: Nougat, port: int) -> Any: ...
    async def test_middleware_must_be_async_function(self, app: Nougat) -> Any: ...
    async def test_middleware_can_be_async_call(self, app: Nougat) -> Any: ...
    async def test_middleware_params_out_of_boundary(self, app: Nougat) -> Any: ...
