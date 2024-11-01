// Função para simular a recuperação de senha
function recoverPassword() {
    alert("Redirecionando para a recuperação de senha...");
    // Aqui você pode adicionar a lógica para redirecionar ou abrir uma nova página para recuperar a senha
}

// Função de validação de login
document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o envio do formulário para validação

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("error-message");

    if (username === "" || password === "") {
        errorMessage.textContent = "Por favor, preencha todos os campos.";
        return;
    }

    // Simulação de autenticação
    if (username === "usuario" && password === "senha123") {
        alert("Login bem-sucedido! Bem-vindo!");
        errorMessage.textContent = "";
        // Redirecionar para a página inicial ou área do usuário
    } else {
        errorMessage.textContent = "Usuário ou senha incorretos.";
    }
});
