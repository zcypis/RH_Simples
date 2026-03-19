from typing import Callable

# --- Filtro & Trasformador ------
def filtrar(funcionarios: list[dict], regra: Callable[[dict], bool]) -> list:
    if not isinstance(funcionarios, list):
        raise TypeError(
            f'esperado list, recebido: {type(funcionarios).__name__}'
        )
    if not funcionarios:
        raise ValueError(
            'lista de funcionarios vazia'
        )
    resultado = []
    for x in funcionarios:
        if regra(x):
            resultado.append(x)

    if not resultado:
        raise ValueError(
            'Nenhum funcionario se encaixa na regra'
        )
    return resultado


def transformar(funcionarios: list[dict], funcao: Callable[[dict], dict]) -> list:
    if not isinstance(funcionarios, list):
        raise TypeError(
            f'esperado list, recebido: {type(funcionarios).__name__}'
        )
    if not funcionarios:
        raise ValueError(
            'lista de funcionarios vazia'
        )
    return [funcao(x) for x in funcionarios]
