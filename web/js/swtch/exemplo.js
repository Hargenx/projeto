let tipofruta = 'Manga';
switch (tipofruta) {
    case "Laranja":
        console.log("O quilo da laranja está R$3,59.");
        break;
    case "Maçã":
        console.log("O quilo da maçã está R$1,32.");
        break;
    case "Banana":
        console.log("O quilo da banana está R$2,48.");
        break;
    case "Cereja":
        console.log("O quilo da cereja está R$3,00.");
        break;
    case "Manga":
        console.log("O quilo da manga está R$5,56.");
        break;
    case "Mamão":
        console.log("O quilo do mamão está R$4,23.");
        break;
    default:
        console.log(`Desculpe, não temos ${tipofruta} .`);
}

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Digite seu nome: ', function (nome) {
    console.log(`Olá, ${nome}!`);
    rl.close();
});

const MIN = 1;
const MAX = 12;

let numeroSecreto = Math.floor(Math.random() * (MAX - MIN + 1)) + MIN;
let tentativas = 0;
let dicas = '';
let numero = 0;

do {
    let input = window.prompt(`Digite um número entre ${MIN} e ${MAX} ${dicas}`);
    numero = parseInt(input);
    tentativas++;
    if (numero > numeroSecreto) {
        dicas = `\nO número é menor que ${numero}`;
    } else if (numero < numeroSecreto) {
        dicas = `\nO número é maior que ${numero}`;
    } else {
        let output = document.createElement('div');
        output.textContent = `Parabéns, você acertou o número secreto em ${tentativas} tentativas!`;
        document.body.appendChild(output);
    }
} while (numero !== numeroSecreto);