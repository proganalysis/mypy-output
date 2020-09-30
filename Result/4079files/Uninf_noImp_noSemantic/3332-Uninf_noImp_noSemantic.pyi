import asyncio
from mpf.core.machine import MachineController
from mpf.devices.ball_device.ball_device import BallDevice
from typing import Any

MYPY: bool

class BallDeviceEjector:
    __slots__: Any = ...
    config: Any = ...
    ball_device: Any = ...
    machine: Any = ...
    def __init__(self, config: dict, ball_device: BallDevice, machine: MachineController) -> None: ...
    @asyncio.coroutine
    def eject_one_ball(self, is_jammed: Any, eject_try: Any) -> None: ...
    @asyncio.coroutine
    def reorder_balls(self) -> None: ...
    def ball_search(self, phase: Any, iteration: Any) -> None: ...
