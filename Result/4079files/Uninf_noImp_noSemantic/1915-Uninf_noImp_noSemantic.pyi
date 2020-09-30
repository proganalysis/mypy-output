import unittest
from typing import Any, Union

class Prostokat:
    bok_a: Any = ...
    bok_b: Any = ...
    def __init__(self, bok_a: Union[float, int], bok_b: [float, int]) -> None: ...
    def pole(self) -> float: ...
    def obwod(self) -> float: ...
    def __str__(self) -> str: ...

class ProstokatTest(unittest.TestCase):
    prostokat: Any = ...
    def setUp(self) -> None: ...
    def test_poprawnego_tworzenie_prostokata(self) -> None: ...
    def test_prostokata_bok_nieprawidlowy(self) -> None: ...
    def test_prostokata_bok_zero(self) -> None: ...
    def test_prostokata_bok_ujemny(self) -> None: ...
    def test_ustawienia_jednego_boku(self) -> None: ...
    def test_przechowywanie_wartosci(self) -> None: ...
    def test_tworzenie_prostokata(self) -> None: ...
    def test_pola(self) -> None: ...
    def test_obwod(self) -> None: ...
    def test_prostokat_to_string(self) -> None: ...