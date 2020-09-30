import pure_interface
import unittest
from typing import Any

class ISpeaker(pure_interface.PureInterface):
    def speak(self, volume: Any) -> None: ...

class ISleepTalker(ISpeaker):
    is_asleep: Any = ...

class Speaker:
    def speak(self, volume: Any): ...

class Talker:
    def talk(self): ...

class TalkerToSpeaker(pure_interface.Concrete, ISpeaker):
    _talker: Any = ...
    def __init__(self, talker: Any) -> None: ...
    def speak(self, volume: Any): ...

class Talker2:
    def talk(self): ...

class TalkerToSpeaker2:
    _talker: Any = ...
    def __init__(self, talker: Any) -> None: ...
    def speak(self, volume: Any): ...

class TalkerToSpeaker3:
    _talker: Any = ...
    def __init__(self, talker: Any) -> None: ...
    def speak(self, volume: Any): ...

class Talker3:
    def talk(self): ...

def talk_to_speaker(talker: Any): ...
def none_to_speaker(_none: Any): ...

class Talker4:
    def talk(self): ...

def bad_adapter(talker: Any): ...

class ITopicSpeaker(ISpeaker):
    @property
    def topic(self) -> None: ...

class TopicSpeaker(Speaker, ITopicSpeaker):
    topic: Any = ...
    def __init__(self, topic: Any) -> None: ...

class Sleeper:
    is_asleep: bool = ...

class SleepTalker(pure_interface.Concrete, ISleepTalker):
    _sleeper: Any = ...
    is_asleep: Any = ...
    def __init__(self, sleeper: Any) -> None: ...
    def speak(self, volume: Any) -> None: ...

class TestAdaption(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_adaption_passes(self) -> None: ...
    def test_implicit_adapter(self) -> None: ...
    def test_callable_adapter_passes(self) -> None: ...
    def test_adapter_call_check(self) -> None: ...
    def test_adapter_check(self) -> None: ...
    def test_from_type_check(self) -> None: ...
    def test_to_interface_check(self) -> None: ...
    def test_adapt_to_interface_raises(self) -> None: ...
    def test_adapt_to_interface_or_none(self) -> None: ...
    def test_no_interface_on_class_raises(self) -> None: ...
    def test_adapt_on_class_works(self) -> None: ...
    def test_filter_adapt(self) -> None: ...
    def test_implicit_filter_adapt(self) -> None: ...

class TestAdaptionToInterfaceOnly(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_wrapping_works(self) -> None: ...
    def test_wrapping_works2(self) -> None: ...
    def test_implicit_adapter_passes(self) -> None: ...
    def test_callable_adapter_passes(self) -> None: ...
    def test_adapt_to_interface_or_none(self) -> None: ...
    def test_filter_adapt(self) -> None: ...
    def test_implicit_filter_adapt(self) -> None: ...
    def test_adapter_to_sub_interface_used(self) -> None: ...
    foo: Any = ...
    def test_adapter_preference(self) -> None: ...
    def test_optional_adapt(self) -> None: ...