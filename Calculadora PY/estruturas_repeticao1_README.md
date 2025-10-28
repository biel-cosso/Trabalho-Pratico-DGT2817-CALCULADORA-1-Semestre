# estruturas_repeticao1.py — README

Descrição
--------
Exemplo de laço `while` que solicita entradas do usuário repetidamente até que ele digite `0`.

Como executar
---------------
```powershell
python "estruturas_repeticao1.py"
```

Comportamento
-------------
- O script inicializa `entrada_idade = ''` e entra em um `while` que pede ao usuário um valor e imprime `Número digitado:` até que a entrada seja exatamente `'0'`.

Notas
-----
- O script compara a string da entrada com `'0'`, portanto entradas como `0` (quando convertidas por `int`) não são usadas — o comportamento é apropriado para leitura de texto.
- Para permitir verificação numérica, você pode converter a entrada para `int` dentro de um bloco `try/except`.
