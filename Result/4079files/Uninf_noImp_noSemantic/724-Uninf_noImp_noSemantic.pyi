from IPython import embed as embed
from pyontutils.core import makeGraph as makeGraph, qname as qname
from typing import Any, List

def convert_view_text_to_dict() -> dict: ...
def get_curies_from_scigraph_label_query(label: str, prefixes: List[str]=...) -> list: ...
def normalize_term(term: Any, prefix: str = ...): ...
def linearize_graph(dict_: dict, tier_level: int=...) -> tuple: ...
def pair_terms(terms: Any): ...
def main() -> None: ...