import hashlib
from dataBaseModule import Database

# Classe responsável pela autenticação de usuários
class Auth:
    
    def __init__(self):
        self.db = Database()  # Conexão com o banco de dados

    def hash_password(self, password):
        # Gera um hash SHA-256 para a senha
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, name, email, password):
        hashed_password = self.hash_password(password)
        user_id = self.db.create_user(name, email, hashed_password)
        
        if user_id:
            print(f"Usuario {name} registrado com o ID {user_id}")
        else:
            print("Falha ao se registrar")

    def login_user(self, email, password):
        user = self.db.get_user(email)
        
        if user:
            stored_password = user[3]
            
            if stored_password == self.hash_password(password):
                print("Logado com sucesso")
                return user
            else:
                print("Senha incorreta")
        else:
            print("Usuario não encontrado")

    def close_connection(self):
        self.db.close()  # Fecha a conexão com o banco de dados
