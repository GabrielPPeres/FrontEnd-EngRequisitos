from authModule import Auth

def main():
    auth = Auth()

    while True:
        print("\n1. Registrar")
        print("2. Login")
        print("3. Sair")
        
        choice = input("Escolha uma opção: ")

        try:
            if choice == '1':
                name = input("Digite o seu nome: ")
                email = input("Digite o seu e-mail: ")
                password = input("Crie uma senha: ")
                auth.register_user(name, email, password)

            elif choice == '2':
                email = input("Digite o seu e-mail: ")
                password = input("Digite a sua senha: ")
                if auth.login_user(email, password):
                    print("Login realizado com sucesso!")
                else:
                    print("Falha no login. Verifique seu email e senha.")

            elif choice == '3':
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    auth.close_connection()

if __name__ == "__main__":
    main()
