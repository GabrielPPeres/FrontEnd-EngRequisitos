document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Previne o envio normal do formulário
    
    // Captura os dados do formulário manualmente
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    // Cria o corpo da requisição com URLSearchParams
    const body = new URLSearchParams();
    body.append('name', name);
    body.append('email', email);
    body.append('password', password);
    
    // Faz a requisição para o servidor Flask
    fetch('http://127.0.0.1:5000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: body,
    })
    .then(response => {
        if (!response.ok) {
            // Se a resposta não for ok (status != 2xx), exibe o erro
            return response.json().then(data => {
                throw new Error(data.message || 'Erro desconhecido');
            });
        }
        return response.json();  // Se ok, retorna o JSON
    })
    .then(data => {
        if (data.status === 'success') {
            alert(data.message);  // Exibe a mensagem de sucesso
            window.location.href = 'http://127.0.0.1:5500/login.html';  // Redireciona para a página de login
        } else {
            alert('Erro: ' + data.message);  // Exibe mensagem de erro recebida do servidor
        }
    })
    .catch(error => {
        // Se ocorrer um erro no frontend ou no backend, exibe uma mensagem genérica
        document.getElementById("error-message").textContent = error.message;  // Exibe erro detalhado
    });
});
