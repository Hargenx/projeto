function nomeDaFuncao(parametro1, parametro2) {
    // Código a ser executado
    return resultado; // Opcional
}

function saudacao(nome) {
    return "Olá, " + nome + "!";
}

let mensagem = saudacao("Raphael");
console.log(mensagem); // Saída: Olá, Raphael!


function soma(a, b) {
    var resultado = a + b;
    return resultado;
}

//console.log(resultado); // Erro: resultado não está definido

let quadrado = function (x) {
    return x * x;
};

console.log(quadrado(2)); // Saída: 4


let dobrar1 = (x) => x * 2;

console.log(dobrar1(8)); // Saída: 16


var dobrar3 = (x) => x * 2;
dobrar3 = (x) => x * 3; // Isso é permitido


let dobrar2 = (x) => x * 2;
// let dobrar = (x) => x * 3; // Isso geraria um erro, pois não é permitido redeclarar no mesmo bloco
dobrar2 = (x) => x * 3; // Isso é permitido, pois é uma reatribuição

const dobrar = (x) => x * 2;
console.log(dobrar(7)); // Saída: 14


function testandoNumero(a) {
    let resultado;
    if (a > 0) {
        resultado = 'Positivo';
    } else {
        resultado = 'Negativo';
    }
    return resultado;
}
console.log(testandoNumero(-1));


let interacao = 0;
top: for (let i = 0; i < 6; i++) {
    for (let j = 0; j < 6; j++) {
        interacao++;
        if (i == 2 && j == 2) {
            break top;
        }
    }
}
console.log(interacao);
