// Obtenha o botão de abrir o modal e o modal em si
const abrirBotaoModal = document.getElementById("abrirBotaoModal");
const modal = document.getElementById("meuModal");

// Obtenha o elemento para fechar o modal (o "x")
const fecharBotao = document.getElementsByClassName("fechar")[0];

// Quando o botão de abrir o modal for clicado, exiba o modal
abrirBotaoModal.addEventListener("click", () => {
    modal.style.display = "block";
});

// Quando o usuário clicar no elemento de fechamento (o "x"), feche o modal
fecharBotao.addEventListener("click", () => {
    modal.style.display = "none";
});

// Quando o usuário clicar fora do modal, feche-o também
window.addEventListener("click", (event) => {
    if (event.target == modal) {
        modal.style.display = "none";
    }
});
