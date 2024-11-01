document.getElementById("forgotPasswordForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o envio do formulário

    const email = document.getElementById("email").value;
    const confirmationMessage = document.getElementById("confirmation-message");

    if (email === "") {
        confirmationMessage.textContent = "Por favor, insira seu e-mail.";
        confirmationMessage.style.color = "red";
        return;
    }

    // Simulação de envio de e-mail de recuperação de senha
    confirmationMessage.textContent = "Instruções de recuperação de senha foram enviadas para o seu e-mail.";
    confirmationMessage.style.color = "green";
});
