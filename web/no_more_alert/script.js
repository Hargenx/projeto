const texto = document.getElementById('entrada');
const escreveTexto = document.getElementById('escreveTexto');

function mudaTexto() {
    const texto_indo = texto.value;
    escreveTexto.textContent = `Texto digitado: ${texto_indo}`;
}