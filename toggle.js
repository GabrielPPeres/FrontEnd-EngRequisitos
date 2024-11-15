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
    }
}
