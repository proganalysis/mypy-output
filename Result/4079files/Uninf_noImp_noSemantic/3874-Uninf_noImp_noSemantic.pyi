from config import *
from typing import Any

class KeyType:
    SMALLEST: int = ...
    RANDOM: int = ...
    LARGEST: int = ...

def keygen(kt: Any = ...): ...
def encrypt(sk: Any, b: Any, mbits: Any = ...): ...
def encryptD(sk: Any, b: Any, mbits: Any = ...): ...
def decrypt(sk: Any, c: Any): ...
def noise(sk: Any, c: Any): ...
def noiseQ(sk: Any, c: Any, q: Any): ...