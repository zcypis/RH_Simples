#  RH Simples – Sistema de Gestão de Funcionários

Sistema de gerenciamento de dados de funcionários via terminal, desenvolvido em Python puro. Permite cadastrar, filtrar, transformar e gerar relatórios com base em critérios como cargo, salário ou departamento — tudo persistido localmente sem dependências externas.

---

## Funcionalidades

- Criar filtros personalizados (por cargo, faixa salarial, departamento, etc.)
- Aplicar transformações nos dados (ex.: ajuste salarial, mascarar informações)
- Gerar relatórios completos ou filtrados da equipe

---

## Critério de classificação (exemplo)

| Faixa salarial (R$) | Classificação |
|---------------------|---------------|
| Até 3.000           | Júnior        |
| 3.001 a 7.000       | Pleno         |
| Acima de 7.000      | Sênior        |

> *Os critérios podem ser alterados ou expandidos nos módulos de filtro.*

---

## Estrutura do projeto

```
relatorio_funcionarios/
- dados_funcionarios.py       # Persistência: carregar e salvar dados em JSON
- criar_filtros.py            # Definição e criação de filtros
- filtrar_transformar.py      # Aplicação de filtros e transformações
- relatorio_funcionarios.py   # Geração de relatórios (entrada principal)
- test_rh.py                  # Testes automatizados
- funcionarios.json           # Banco de dados local (gerado automaticamente)
- .gitignore
- README.md
```

---

## Como usar

### Pré-requisitos
- Python 3.10 ou superior

### Executando o projeto

```bash
git clone https://github.com/zcypis/RH_Simples.git
cd RH_Simples
python relatorio_funcionarios.py
```

### Gerar relario

Ao executar relatorio_funcionarios.py, gera um relatorio de: dados_funcionarios.py

---

## Arquitetura
O projeto segue o princípio de separação de **responsabilidades** — cada módulo tem uma função clara e independente:

| Módulo | Responsabilidade |
|---|---|
| `dados_funcionarios.py`     | Abstrai o carregamento e salvamento do arquivo JSON
| `criar_filtros.py`          | Contém funções para construir filtros dinâmicos
| `filtrar_transformar.py`    | Aplica filtros e transformações nos dados carregados
| `relatorio_funcionarios.py` | Orquestra o menu e gera saídas formatadas
| `test_rh.py`                | Testes unitários para garantir a integridade do sistema

---

## 🛠️ Tecnologias

- Python 3.10+
- Somente biblioteca padrão — `typing` e `time`
- Sem dependências externas

---

## 👨‍💻 Autor

**Guilherme Xavier**
- GitHub: [@zcypis](https://github.com/zcypis)
- Email: guilhermexavie3@gmail.com