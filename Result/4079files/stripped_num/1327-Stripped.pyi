# (generated with --quick)

import json.encoder
from typing import Any, Callable, Generator, List, Optional, Tuple, Type, TypeVar, Union

pygame: Any
select: module
socket: module

_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T4 = TypeVar('_T4')

def __getattr__(name) -> Any: ...
def boucle(commandes, combats: _T1, ids, joueurs, joueurs_a_supprimer: _T4) -> Tuple[Any, Any, _T1, _T4]: ...
def carte(id_joueur, joueurs) -> Optional[str]: ...
def commandecarte(message, client, ids, joueurs, combats) -> Tuple[Any, Any]: ...
def commandecombat(message, client, joueurs: _T2) -> _T2: ...
def connexion(client, ids, joueurs: _T2) -> Tuple[Any, _T2]: ...
def dumps(obj, skipkeys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., cls: Optional[Type[json.encoder.JSONEncoder]] = ..., indent: Optional[Union[int, str]] = ..., separators: Optional[Tuple[str, str]] = ..., default: Optional[Callable[[Any], Any]] = ..., sort_keys: bool = ..., **kwds) -> str: ...
def entitee_combat(id, joueurs) -> str: ...
def lancer_sort(joueur, sort, cible, joueurs) -> Any: ...
def lire_message() -> Generator[List[Tuple[Any, Any]], Any, nothing]: ...
def main() -> Any: ...
def mouvement(idjoueur, direction, joueurs, combat) -> Any: ...
def mouvement_combat(idjoueur, direction, joueurs) -> Any: ...
