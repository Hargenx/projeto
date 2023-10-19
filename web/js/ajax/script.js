function getPrevisaoTempo() {
    const entradaCidade = document.getElementById("cidade");
    const nomeCidade = entradaCidade.value;
    const API_KEY = "b1b15e88fa797225412429c1c50c122a1"
  
    // Verifica se o campo de entrada está vazio
    if (nomeCidade === "") {
      alert("Por favor, digite o nome da cidade.");
      return;
    }
  
    const resultadoPrevisao = document.getElementById("resultado-previsao");
  
    // Cria uma instância do objeto XMLHttpRequest
    const xhr = new XMLHttpRequest();
  
    // Configura a solicitação
    xhr.open("GET", `https://api.openweathermap.org/geo/1.0/direct?q=${nomeCidade}&appid=${API_KEY}`, true);
  
    // Define o que fazer quando a resposta é recebida
    xhr.onload = function () {
      if (xhr.status === 200) {
        const dados = JSON.parse(xhr.responseText);
        const descricaoTempo = dados.weather.description;
        const temperatura = (dados.main.temp - 273.15).toFixed(2);
  
        resultadoPrevisao.innerHTML = `Previsão do tempo em ${nomeCidade}: ${descricaoTempo}. Temperatura: ${temperatura}°C`;
      } else if (xhr.status === 401) {
        resultadoPrevisao.innerHTML = "Sem retorno"
      }else{
        resultadoPrevisao.innerHTML = "Cidade não encontrada. Verifique o nome e tente novamente.";
      }
    };
  
    // Envia a solicitação
    xhr.send();
  }
  