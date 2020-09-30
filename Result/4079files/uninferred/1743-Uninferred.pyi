from json import JSONEncoder
from typing import Any

class LeiauteEncoder(JSONEncoder):
    def default(self, o: Any): ...

def normalize_spaces(s: Any): ...
def normalize_quotes(s: Any): ...
def remove_space(s: Any): ...
def extrair_parametros(s: Any): ...

class Leiaute:
    tipo: Any = ...
    versao: Any = ...
    data_inicio: Any = ...
    blocos: Any = ...
    registros: Any = ...
    def __init__(self, tipo: Any, versao: Any, data_inicio: Any, blocos: Any, registros: Any) -> None: ...

class Bloco:
    nome: Any = ...
    descricao: Any = ...
    def __init__(self, nome: Any, descricao: Any) -> None: ...
    def __repr__(self): ...

class Registro:
    codigo: Any = ...
    nome: Any = ...
    regras: Any = ...
    nivel: Any = ...
    ocorrencia: Any = ...
    campos_chave: Any = ...
    campos: Any = ...
    def __init__(self, codigo: Any, nome: Any, regras: Any, nivel: Any, ocorrencia: Any, campos_chave: Any) -> None: ...
    def __repr__(self): ...

class Campo:
    indice: Any = ...
    nome: Any = ...
    descricao: Any = ...
    tipo: Any = ...
    tamanho: Any = ...
    decimal: Any = ...
    valores: Any = ...
    obrigatorio: Any = ...
    regras: Any = ...
    def __init__(self, indice: Any, nome: Any, descricao: Any, tipo: Any, tamanho: Any, decimal: Any, valores: Any, obrigatorio: Any, regras: Any) -> None: ...
    def __repr__(self): ...
