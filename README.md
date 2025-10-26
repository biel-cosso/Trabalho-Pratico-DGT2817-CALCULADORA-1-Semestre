# Projetos de Exercícios em Python

Este repositório contém exemplos didáticos em Python que demonstram estruturas condicionais, laços de repetição e funções. Os scripts são curtos, fáceis de ler e destinados ao aprendizado.

## Como usar este README

Este README funciona como índice e documentação principal. Abaixo há uma descrição para cada arquivo do projeto com o que ele faz, como executar e exemplos.

## Como executar (PowerShell)

Abra o PowerShell no diretório deste projeto e rode:

```powershell
python "calculadora_v2.py"
python "estruturas_condicao1.py"
python "estruturas_condicao2.py"
python "estruturas_repeticao1.py"
python "estruturas_repeticao2.py"
python "funcoes2.py"
```

Observação: alguns scripts são interativos e pedem valores via `input()`.

---

## Arquivos e o que cada um faz

- calculadora_v2.py
	- Objetivo: uma calculadora interativa com funções para adição, subtração, multiplicação e divisão.
	- Entradas: dois números (float) e operação (`+`, `-`, `*`, `/` ou nomes das operações).
	- Tratamento: trata `ValueError` para entradas inválidas e verifica divisão por zero.
	- Exemplo rápido:

		Digite o primeiro número: 10
		Digite o segundo número: 2
		Digite a operação desejada: /
		Resultado da operação: 5.0

- estruturas_condicao1.py
	- Objetivo: demonstrar `if/else` usando uma variável `temperatura` (com valor padrão no script).
	- Comportamento: imprime se o dia está ameno ou quente dependendo se `temperatura < 30`.
	- Sugestão: transformar em entrada do usuário para testar diferentes valores.

- estruturas_condicao2.py
	- Objetivo: demonstrar `if/elif/else` classificando nível por `tempoExperiencia`.
	- Observação: a condição atual `elif 2 < tempoExperiencia < 5` não inclui `tempoExperiencia == 2`; para incluir 2, use `elif 2 <= tempoExperiencia < 5`.

- estruturas_repeticao1.py
	- Objetivo: demonstrar `while` lendo entradas até o usuário digitar `0`.
	- Comportamento: imprime cada valor digitado; sai quando a entrada for a string `'0'`.
	- Sugestão: converter para `int` com tratamento de exceções se desejar validação numérica.

- estruturas_repeticao2.py
	- Objetivo: demonstrar `for` iterando sobre uma string e sobre um intervalo com `range(1, 11)`.
	- Observação: o arquivo contém um laço `for` sobre a string repetido; pode-se remover duplicação e tornar a função `imprimir_variavel` reutilizável aceitando parâmetro.

- funcoes2.py
	- Objetivo: demonstrar funções e manipulação de strings com a função `loginUsuario(perfil)`.
	- Comportamento: compara `perfil.lower()` com `'admin'` e imprime saudações diferentes.
	- Sugestão: alterar a função para retornar a mensagem (facilita testes) em vez de imprimir diretamente.

---

## Boas práticas sugeridas

- Encapsular a lógica executável em `main()` e proteger com:

```python
if __name__ == "__main__":
		main()
```

- Extrair funções testáveis e adicionar testes unitários com `pytest` para as operações principais (calculadora, divisão por zero, loginUsuario, etc.).
- Usar `argparse` se quiser permitir execução não interativa por linha de comando.

## Requisitos

- Python 3.x (testado com Python 3.8+)

## Próximos passos que posso executar

- Encapsular scripts em `main()` e aplicar pequenas refatorações.
- Adicionar um arquivo `requirements.txt` (se houver dependências) e testes básicos com `pytest`.
- Fazer commit e push destas mudanças (se você confirmar o caminho do repositório/local onde deseja executar git).

---

Se quiser que eu faça qualquer um dos próximos passos, diga qual prefere e eu executo.

