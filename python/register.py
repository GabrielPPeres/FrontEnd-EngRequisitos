from authModule import Auth  # Importa a classe Auth que você criou

def main():
    auth = Auth()
    name = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    password = input("Digite a senha do usuário: ")
    auth.register_user(name, email, password)
    auth.close_connection()
if __name__ == "__main__":
    main()
