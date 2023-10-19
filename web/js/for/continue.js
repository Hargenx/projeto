let frase = 'Usando continue no Javascript';
let contador = 0;
for (let i = 0; i < frase.length; i++) {
    if (frase.charAt(i) != 's') {
        continue;
    }
    contador++;
}
console.log('O numero de s encontrado na nossa string é: ' + contador);
outer: for (let i = 0; i <= 5; i++) {
    for (let j = 0; j <= 5; j++) {
        if (i == 2 && j == 2) {
            console.log('continue outer');
            continue outer;
        }
        console.log(`[i: ${i} e j: ${j}]`);
    }
}
  