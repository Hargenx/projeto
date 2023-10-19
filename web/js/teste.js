const alunos = [
    { nome: "Raphael", nota: 7 },
    { nome: "Caroline", nota: 9 },
    { nome: "Gilson", nota: 5 },
    { nome: "Sara", nota: 8 },
    { nome: "Vinicius", nota: 6 }
];
const nomesDosAlunos = alunos.map(function (aluno) {
    return aluno.nome;
});
console.log(nomesDosAlunos);
console.log(alunos[4])