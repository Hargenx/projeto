import { estudarMais } from './module.js';

const botaoElement = document.getElementById("botao");

botaoElement.addEventListener("click", function() {
    estudarMais();
    // Oculte o botão após o clique
    botaoElement.style.display = "none";
});