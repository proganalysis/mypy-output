from gensim import corpora
from rtype import NIntArray
from typing import Any, List, Tuple

def ia(lst: List[int]) -> NIntArray: ...
def tokens2ids(tokens: List[str], dictionary: corpora.Dictionary, verbose: bool=...) -> List[int]: ...
def create_dictionary(corpuses: List[str], min_freq: int=..., with_symbol: Any=...) -> corpora.Dictionary: ...
def save_dictionary(dic: corpora.Dictionary, filename: str) -> None: ...
def load_dictionary(filename: str) -> corpora.Dictionary: ...
def load_sentence(filename: str, with_symbol: bool=...) -> List[str]: ...
def load_conversation(filename: str, dictionary: corpora.Dictionary, with_symbol: bool=...) -> Tuple[List[int], List[int]]: ...
