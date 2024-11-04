# test_auth.py
from authModule import Auth

def test_auth_module():
    auth = Auth()

    # Teste de registro de usuário
    print("Iniciando o teste de registro...")
    name = "João"
    email = "joao@example.com"
    password = "senha123"
    auth.register_user(name, email, password)

    # Teste de login com credenciais corretas
    print("Iniciando o teste de login com credenciais corretas...")
    assert auth.login_user(email, password) == True, "Falha ao logar com credenciais corretas."

    # Teste de login com credenciais incorretas
    print("Iniciando o teste de login com credenciais incorretas...")
    assert auth.login_user(email, "senha_errada") == False, "Falha ao detectar credenciais incorretas."

    # Teste de login com usuário não registrado
    print("Iniciando o teste de login com usuário não registrado...")
    assert auth.login_user("usuario_inexistente@example.com", "senha123") == False, "Falha ao detectar usuário não registrado."

    print("Todos os testes passaram com sucesso!")

if __name__ == "__main__":
    test_auth_module()
