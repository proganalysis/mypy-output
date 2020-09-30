from chromewhip.helpers import BaseEvent as BaseEvent, ChromeTypeBase, PayloadMixin
from typing import Any, Optional, Union

log: Any

class GPUDevice(ChromeTypeBase):
    vendorId: Any = ...
    deviceId: Any = ...
    vendorString: Any = ...
    deviceString: Any = ...
    driverVendor: Any = ...
    driverVersion: Any = ...
    def __init__(self, vendorId: Union[float], deviceId: Union[float], vendorString: Union[str], deviceString: Union[str], driverVendor: Union[str], driverVersion: Union[str]) -> None: ...

class Size(ChromeTypeBase):
    width: Any = ...
    height: Any = ...
    def __init__(self, width: Union[int], height: Union[int]) -> None: ...

class VideoDecodeAcceleratorCapability(ChromeTypeBase):
    profile: Any = ...
    maxResolution: Any = ...
    minResolution: Any = ...
    def __init__(self, profile: Union[str], maxResolution: Union[Size], minResolution: Union[Size]) -> None: ...

class VideoEncodeAcceleratorCapability(ChromeTypeBase):
    profile: Any = ...
    maxResolution: Any = ...
    maxFramerateNumerator: Any = ...
    maxFramerateDenominator: Any = ...
    def __init__(self, profile: Union[str], maxResolution: Union[Size], maxFramerateNumerator: Union[int], maxFramerateDenominator: Union[int]) -> None: ...
SubsamplingFormat = str
ImageType = str

class ImageDecodeAcceleratorCapability(ChromeTypeBase):
    imageType: Any = ...
    maxDimensions: Any = ...
    minDimensions: Any = ...
    subsamplings: Any = ...
    def __init__(self, imageType: Union[ImageType], maxDimensions: Union[Size], minDimensions: Union[Size], subsamplings: Union['[SubsamplingFormat]']) -> None: ...

class GPUInfo(ChromeTypeBase):
    devices: Any = ...
    auxAttributes: Any = ...
    featureStatus: Any = ...
    driverBugWorkarounds: Any = ...
    videoDecoding: Any = ...
    videoEncoding: Any = ...
    imageDecoding: Any = ...
    def __init__(self, devices: Union['[GPUDevice]'], driverBugWorkarounds: Union['[]'], videoDecoding: Union['[VideoDecodeAcceleratorCapability]'], videoEncoding: Union['[VideoEncodeAcceleratorCapability]'], imageDecoding: Union['[ImageDecodeAcceleratorCapability]'], auxAttributes: Optional[dict]=..., featureStatus: Optional[dict]=...) -> None: ...

class ProcessInfo(ChromeTypeBase):
    type: Any = ...
    id: Any = ...
    cpuTime: Any = ...
    def __init__(self, type: Union[str], id: Union[int], cpuTime: Union[float]) -> None: ...

class SystemInfo(PayloadMixin):
    @classmethod
    def getInfo(cls): ...
    @classmethod
    def getProcessInfo(cls): ...
