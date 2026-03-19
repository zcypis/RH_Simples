# --- Criar Filtros --------
def fazer_filtro_depto(depto: str):
    if not isinstance(depto, str):
        raise TypeError(
            f'esperado str, recebido: {type(depto).__name__}'
        )
    if not depto.strip():
        raise ValueError(
            'departamento vazio'
        )
    def regra(f: dict) -> bool:

        return f["departamento"] == depto
    return regra


def fazer_filtro_salario(salario: float):
    if not isinstance(salario, (int, float)):
        raise TypeError(
            f'esperado float, recebido: {type(salario).__name__}'
        )
    def regra(f: dict) -> bool:
        if not isinstance(f, dict):
            raise TypeError(
                f'esperado dict, recebido: {type(f).__name__}'
            )

        return f["salario"] > salario
    
    return regra


# --- Regras & Extratores ---------
esta_ativo = lambda f: f["ativo"]

salario_7k = fazer_filtro_salario(7000)

filtro_ti = fazer_filtro_depto("TI")

filtro_vendas = fazer_filtro_depto("Vendas")

filtro_rh = fazer_filtro_depto("RH")

extrair_nome = lambda f: f["nome"]

resumir = lambda f: {'nome': f['nome'], 'departamento': f['departamento'], 'salario': f['salario']}

def aplicar_bonus(f: dict) -> dict:
    return {
        "nome": f["nome"],
        "departamento": f["departamento"],
        "salario": round(f["salario"] * 1.1, 2),
        "ativo": f["ativo"]
    }
