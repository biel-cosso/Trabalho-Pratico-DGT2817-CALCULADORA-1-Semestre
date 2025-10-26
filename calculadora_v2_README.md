# calculadora_v2.py — README

Descrição
--------
Script que implementa uma calculadora interativa simples com as operações básicas: adição, subtração, multiplicação e divisão. Contém funções separadas para cada operação e uma função `calculadora` que escolhe a operação com base na entrada do usuário.

Como executar
---------------
No PowerShell (ou outro terminal), navegue até o diretório e execute:

```powershell
python "calculadora_v2.py"
```

Entradas
--------
- Dois números (floats) solicitados via `input()`.
- Uma operação: `+`, `-`, `*`, `/` ou o nome textual da operação (`soma`, `subtracao`, `multiplicacao`, `divisao`).

Saídas
------
- Imprime o resultado da operação ou mensagens de erro (ex.: divisão por zero, entrada inválida).

Exemplo de sessão
------------------
```
Digite o primeiro número: 10
Digite o segundo número: 0
Digite a operação desejada (+, -, *, / ou nome da operação): /
Resultado da operação: Não foi possível realizar a divisão por 0
```

Notas e sugestões
------------------
- O script já trata `ValueError` para entradas não numéricas.
- Sugestão: encapsular a interação em uma função `main()` e proteger com `if __name__ == "__main__": main()` para permitir importação em testes.

Pequenas melhorias sugeridas
- Adicionar testes unitários para funções (por exemplo, `adicao`, `divisao`).
- Usar `argparse` para permitir execução não interativa.
