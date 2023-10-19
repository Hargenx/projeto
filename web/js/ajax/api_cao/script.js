const racaSelect = document.getElementById("raca2");

const racas = [
    "affenpinscher", "african", "airedale", "akita", "appenzeller",
    "australian-shepherd", "basenji", "beagle", "bluetick", "borzoi",
    "bouvier", "boxer", "brabancon", "briard", "buhund-norwegian",
    "bulldog-boston", "bulldog-english", "bulldog-french", "bullterrier-staffordshire"
];

racas.forEach((raca) => {
    const option = document.createElement("option");
    option.value = raca;
    option.textContent = raca;
    racaSelect.appendChild(option);
});

//https://dog.ceo/dog-api/documentation/
function obterImagnsAleatoriasAuAu() {
    const auAu = document.getElementById("resultado-canis");
    const xhr = new XMLHttpRequest();
    const endpoint = "https://dog.ceo/api/breeds/image/random";

    xhr.open("GET", endpoint, true);

    xhr.onload = function () {
        if (xhr.status === 200) {
            const dados = JSON.parse(xhr.responseText);
            const imagemUrl = dados.message;

            auAu.innerHTML = `<img src="${imagemUrl}" alt="Imagem de um cachorro">`;
        } else {
            auAu.innerHTML = "Não foi possível obter uma imagem de cachorro.";
        }
    };

    xhr.send();
}


function obterImagemEscolhida() {
    const auAu = document.getElementById("raca").value;
    const xhr = new XMLHttpRequest();
    let exibe = document.getElementById("mostra")

    xhr.open("GET", `https://dog.ceo/api/breed/${auAu}/images/random`, true);

    xhr.onload = function () {
        if (xhr.status === 200) {
            const dados = JSON.parse(xhr.responseText);
            console.log(dados);
            const caoRaca = dados.message;
            exibe.innerHTML = `<img src="${caoRaca}" alt="Imagem de um cachorro">`;
        } else if (xhr.status > 400) {
            exibe.innerHTML = `Cachorro mau`
        } else {
            exibe.innerHTML = "Cachorro mau 2";
        }
    };
    // Envia a solicitação
    xhr.send();
}