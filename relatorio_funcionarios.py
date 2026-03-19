from typing import Callable
from filtrar_transformar import *
from criar_filtros import *
from dados_funcionarios import funcionarios

# --- Calculos ---------
def media_salarial(funcionarios: list[dict]) -> float:
    if not isinstance(funcionarios, list):
        raise TypeError(
            f'esperado list, recebido: {type(funcionarios).__name__}'
        )
    if not funcionarios:
        raise ValueError(
            'lista de funcionarios vazia'
        )
    return sum([f["salario"] for f in funcionarios]) / len(funcionarios)


maior_salario = lambda f: max(f, key=lambda x: x["salario"])

menor_salario = lambda f: min(f, key=lambda x: x["salario"])


# --- Relatorio ---------
def gerar_relatorio(funcionarios: list[dict]) -> str:
    if not isinstance(funcionarios, list):
        raise TypeError(
            f'esperado list, recebido: {type(funcionarios).__name__}'
        )
    if not funcionarios:
        raise ValueError(
            'lista de funcionarios vazia'
        )
    relatorio = {
        'ativos': len(filtrar(funcionarios, esta_ativo)),
        'salario_medio': media_salarial(funcionarios),
        'salario_maior': maior_salario(funcionarios),
        'salario_menor': menor_salario(funcionarios),
        'funcio_ti': transformar(filtrar(funcionarios, filtro_ti), extrair_nome),
        'funcio_vendas': transformar(filtrar(funcionarios, filtro_vendas), extrair_nome),
        'funcio_rh': transformar(filtrar(funcionarios, filtro_rh), extrair_nome)
    }

    relatorio_str = f'''
        ====== Relatório Funcionários ======
        Funcionários ativos: {relatorio["ativos"]}
        Salário médio: {relatorio["salario_medio"]}
        Maior salário: {relatorio["salario_maior"]["nome"]} - {relatorio["salario_maior"]["salario"]}
        Menor salário: {relatorio["salario_menor"]["nome"]} - {relatorio["salario_menor"]["salario"]}

        ====== Departamentos ======
        Funcionários TI: {", ".join(relatorio["funcio_ti"])}
        Funcionários Vendas: {", ".join(relatorio["funcio_vendas"])}
        Funcionários RH: {", ".join(relatorio["funcio_rh"])}
    '''
    return relatorio_str


if __name__ == '__main__':
    print(gerar_relatorio(funcionarios))
