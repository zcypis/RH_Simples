from criar_filtros import aplicar_bonus, fazer_filtro_salario
from dados_funcionarios import funcionarios
from filtrar_transformar import transformar, filtrar
from time import sleep


def executar_testes():
    print("=== Iniciando Testes do Sistema RH ===\n")

    sleep(1)

    print("Teste 1: Aplicando bônus de 10%...")
    func_teste = {"nome": "Teste", "departamento": "TI", "salario": 1000, "ativo": True}
    resultado = aplicar_bonus(func_teste)
    
    if resultado["salario"] == 1100.0:
        print("Sucesso: Bônus calculado corretamente (1000 -> 1100).")

    else:
        print(f"Falha: Salário esperado 1100.0, recebido {resultado['salario']}.")

    sleep(2)

    print("\nTeste 2: Aplicando bônus em toda a lista...")

    try:
        lista_com_bonus = transformar(funcionarios, aplicar_bonus)
        print(f"Sucesso: {len(lista_com_bonus)} funcionários processados.")

    except Exception as e:
        print(f"Falha ao transformar lista: {e}")

    sleep(2)

    print("\nTeste 3: Filtrando salários acima de 9000...")

    salario_alto = fazer_filtro_salario(9000)

    try:
        ricos = filtrar(funcionarios, salario_alto)
        nomes = [f["nome"] for f in ricos]
        print(f"Sucesso: Encontrados {len(nomes)} funcionários ({', '.join(nomes)}).")

    except ValueError:
        print("Falha: Deveria haver funcionários com mais de 9000.")

    sleep(2)

    print("\nTeste 4: Validação de erro (enviando tipo errado para filtro)...")

    try:
        fazer_filtro_salario("texto_em_vez_de_numero")
        print("Falha: O sistema deveria ter lançado um TypeError.")

    except TypeError:
        print("Sucesso: O sistema barrou a entrada de string no salário corretamente.")
    
    sleep(2)

    print("\n=== Testes Finalizados ===")


if __name__ == '__main__':
    executar_testes()