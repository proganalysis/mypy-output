# (generated with --quick)

from typing import Any

class Object:
    __dict__: Any
    def __init__(self, attributes) -> None: ...

class ObjectLayout:
    def DeliveryDetails(Module: ObjectLayout, ModuleTo, Service, Server, Channel) -> Object: ...
    def message(Contents: ObjectLayout, Author, Server, Channel, Service, Roles, User = ..., profilePicture = ..., emojis = ...) -> Object: ...
    def sendMsgDeliveryDetails(Message: ObjectLayout, DeliveryDetails, FormattingOptions, messageUnchanged, formattingSettings = ..., formatType = ..., customArgs = ...) -> Object: ...
