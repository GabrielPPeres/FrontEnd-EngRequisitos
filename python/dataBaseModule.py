import psycopg2

# Classe responsável pela interação com o banco de dados
class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="login",
            user="postgres",
            password="1234"
        )
        self.cursor = self.connection.cursor()

    def create_user(self, name, email, password):
        try:
            self.cursor.execute(
                """
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
                RETURNING id;
                """, (name, email, password)
            )
            user_id = self.cursor.fetchone()[0]
            self.connection.commit()
            return user_id
        except Exception as e:
            print(f"Error creating user: {e}")
            self.connection.rollback()
            return None  # Retorna None em caso de erro

    def get_user(self, email):
        try:
            self.cursor.execute(
                """
                SELECT * FROM users WHERE email = %s;
                """, (email,)
            )
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error retrieving user: {e}")
            return None

    def close(self):
        # Fecha o cursor e a conexão com o banco de dados
        self.cursor.close()
        self.connection.close()
