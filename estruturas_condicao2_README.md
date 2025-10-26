# estruturas_condicao2.py — README

Descrição
--------
Exemplo de uso de `if/elif/else` para classificar um nível de conhecimento com base em `tempoExperiencia`.

Como executar
---------------
```powershell
python "estruturas_condicao2.py"
```

Comportamento atual
-------------------
- Define `tempoExperiencia = 3` e então testa:
  - `if tempoExperiencia < 2`: júnior
  - `elif 2 < tempoExperiencia < 5`: pleno
  - `else`: sênior

Observação importante
---------------------
- A condição `elif 2 < tempoExperiencia < 5` não inclui `tempoExperiencia == 2`. Se quiser que 2 seja considerado pleno, altere para `elif 2 <= tempoExperiencia < 5`.

Sugestões
---------
- Tornar `tempoExperiencia` entrada do usuário para testar facilmente outros valores.
- Encapsular em `main()` e adicionar validação de tipo.
