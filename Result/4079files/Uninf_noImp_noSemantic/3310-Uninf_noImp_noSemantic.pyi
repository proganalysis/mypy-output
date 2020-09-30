class ExampleClass:
    PUBLIC: int = ...
    _HIDDEN: int = ...
    __PRIVATE: int = ...
    public: int = ...
    _hidden: int = ...
    __private: int = ...
    def __init__(self) -> None: ...

class ExampleTrait:
    @staticmethod
    def static_method(): ...
    @classmethod
    def class_method(cls): ...
    def instance_method(self): ...
