from flask import Flask, request, jsonify
from authModule import Auth
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

auth = Auth()

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')

    if auth.login_user(username, password):
        return jsonify({'message': 'Login realizado com sucesso!'}), 200
    else:
        return jsonify({'message': 'Falha no login. Verifique seu email e senha.'}), 401
    
@app.route('/register', methods=['POST'])
def register():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    auth.register_user(name, email, password)
    return jsonify({'message': 'Usuário registrado com sucesso!'}), 201


if __name__ == "__main__":
    app.run(debug=True)
