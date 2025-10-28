def loginUsuario(perfil):
    # Converte o valor para letras minúsculas antes de comparar
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chamadas da função com diferentes variações
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('ADMIN')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('Outro')
