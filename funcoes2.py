def loginUsuario(perfil):
    # Verifica se o perfil é igual a 'admin' (ignorando maiúsculas/minúsculas)
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chamadas da função com diferentes valores de parâmetro
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')