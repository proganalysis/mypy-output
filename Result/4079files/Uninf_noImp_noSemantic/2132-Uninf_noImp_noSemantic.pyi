from stoq.data_classes import StoqResponse
from stoq.plugins import DecoratorPlugin

class DummyDecorator(DecoratorPlugin):
    def decorate(self, response: StoqResponse) -> None: ...
