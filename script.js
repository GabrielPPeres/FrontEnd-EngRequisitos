document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o envio normal do formulário

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'username': username,
            'password': password
        })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                throw new Error(data.message || 'Erro no login'); // Captura a mensagem do backend
            });
        }
        return response.json();
    })
    .then(data => {
        alert(data.message); // Exibe a mensagem de sucesso
        // Aqui você pode redirecionar ou fazer algo após o login bem-sucedido
    })
    .catch(error => {
        document.getElementById("error-message").textContent = error.message; // Exibe a mensagem de erro
    });
});
