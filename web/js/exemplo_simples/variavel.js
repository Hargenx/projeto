let funcao = [];
for (var i = 0; i < 3; i++) {
    funcao[i] = function () {
        console.log(i);
    };
}
for (let j = 0; j < 3; j++) {
    funcao[j]();
}
