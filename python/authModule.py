from dataBaseModule import Database

# Classe de autenticacao do user
class Auth:
    
    def __init__(self):
        self.db = Database()  # conecta no banco de dados utilizando a classe do arquivo dataBaseModule.py

    def simple_hash(self, password):
        #criptografa a senha (criptografia basica, sem uso real)
        hashed = 0
        for char in password:
            hashed += ord(char)  # Soma o valor ASCII de cada caractere
        return str(hashed)  # Converte o resultado para string

    def register_user(self, name, email, password):
        #registra um novo user no banco de dados
        hashed_password = self.simple_hash(password)  # Usar a função simple_hash para criptografar a senha
        user_id = self.db.create_user(name, email, hashed_password)
        
        if user_id:
            print(f"Usuário {name} registrado com o ID {user_id}")
        else:
            print("Falha ao se registrar")

    def login_user(self, email, password):
        """Realiza o login de um usuário utilizando o e-mail e a senha fornecidos."""
        user = self.db.get_user(email)
        
        if user:
            stored_password = user[3]  # Presume que a senha está na posição 3 do retorno
            
            if stored_password == self.simple_hash(password):  # Usar a função simple_hash
                print("Logado com sucesso")
                return True  # Retorna True se o login for bem-sucedido
            else:
                print("Senha incorreta")
                return False  # Retorna False se a senha estiver incorreta
        else:
            print("Usuário não encontrado")
            return False  # Retorna False se o usuário não for encontrado

    def close_connection(self):
        """Fecha a conexão com o banco de dados."""
        self.db.close()  # Fecha a conexão com o banco de dados
