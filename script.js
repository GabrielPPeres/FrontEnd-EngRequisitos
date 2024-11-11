// Código existente para o envio do formulário de login
document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o envio normal do formulário

    const username = document.getElementById("email").value;
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

// Função para alternar entre as seções de login e cadastro
function toggleSections() {
    const loginSection = document.getElementById("loginSection");
    const signupSection = document.getElementById("signupSection");
    const welcomeTitle = document.getElementById("welcomeTitle");
    const welcomeMessage = document.getElementById("welcomeMessage");
    const toggleButton = document.getElementById("toggleButton");
    const container = document.getElementById("container");

    // Alterna entre mostrar/esconder as seções
    if (loginSection.style.display === "none") {
        // Exibe a seção de login e esconde a de cadastro
        loginSection.style.display = "block";
        signupSection.style.display = "none";

        // Altera o texto de boas-vindas e o botão para "Cadastrar"
        welcomeTitle.textContent = "Olá!";
        welcomeMessage.textContent = "Registre-se com seus dados para acessar todas as funcionalidades";
        toggleButton.textContent = "Cadastrar";

        // Remove a classe de inversão de layout para voltar ao estado original
        container.classList.remove("invert-layout");
    } else {
        // Exibe a seção de cadastro e esconde a de login
        loginSection.style.display = "none";
        signupSection.style.display = "block";

        // Altera o texto de boas-vindas e o botão para "Login"
        welcomeTitle.textContent = "Bem-vindo!";
        welcomeMessage.textContent = "Já possui uma conta? Clique no botão abaixo para voltar ao login.";
        toggleButton.textContent = "Login";

        // Adiciona a classe para inverter o layout
        container.classList.add("invert-layout");
    }
}
