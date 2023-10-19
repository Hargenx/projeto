let soma = 0;
for (var i = 0; i <= 9; i++, soma += i)
    console.log(`Valor de i: ${i}
valor de soma: ${soma}`);
console.log(`Valor final: soma -> ${soma} e i -> ${i}`);

for (var contador = 1; contador <= 10; contador++) {
    console.log('Dentro do loop: ' + contador);
}
console.log('Fora do loop: ' + contador);

let j = 1;
for (; j < 10; j += 2) {
    console.log(j);
}

for (let j = 1; ; j += 2) {
    console.log(j);
    if (j > 10) {
        break;
    }
}


let jw = 1;
for (; ;) {
    console.log(jw);
    if (jw > 10) break;
    console.log(jw);
    jw += 2;
}

const pi = 3.14;
var soma1 = 0;
for (let i = 1; i <= 10; i++) {
    soma1 += 1;
}
if (soma1 > 10) {
    let somaPi = soma1 + pi;
    var maisUm = somaPi + 1;
    console.log(somaPi);
}
console.log(maisUm);
console.log(soma1);

