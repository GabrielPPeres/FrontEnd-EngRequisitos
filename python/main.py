from flask import Flask, request, jsonify
from authModule import Auth
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas nao meche nesta merda da erro pra krl

auth = Auth()

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')

    # Validação básica
    if not username or not password:
        return jsonify({'message': 'Usuário e senha são obrigatórios.'}), 400

    if auth.login_user(username, password):
        return jsonify({'status': 'success', 'message': 'Login realizado com sucesso!'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Falha no login. Verifique seu email e senha.'}), 401
    
@app.route('/register', methods=['POST'])
def register():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Validação básica
    if not name or not email or not password:
        return jsonify({'message': 'Nome, email e senha são obrigatórios.'}), 400

    try:
        auth.register_user(name, email, password)
        return jsonify({'status': 'success', 'message': 'Usuário registrado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Falha ao registrar usuário.', 'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
