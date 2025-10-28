# funcoes2.py — README

Descrição
--------
Arquivo com a função `loginUsuario(perfil)` que demonstra comparação de strings (uso de `str.lower()`) para diferenciar um perfil `admin` de outros perfis e imprimir uma saudação apropriada. O arquivo contém chamadas de exemplo com diferentes capitalizações.

Como executar
---------------
```powershell
python "funcoes2.py"
```

Comportamento
-------------
- A função transforma o argumento `perfil` para letras minúsculas e compara com `'admin'`. Se coincidir, imprime `Bem-vindo, Administrador`, caso contrário `Bem-vindo, Usuário`.
- O script chama a função várias vezes com entradas como `'Admin'`, `'admin'`, `'ADMIN'`, `'User'`, etc., demonstrando que o `lower()` normaliza a comparação.

