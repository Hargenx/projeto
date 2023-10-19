const alunos = [
    { nome: "Raphael", nota: 7 },
    { nome: "Caroline", nota: 9 },
    { nome: "Gilson", nota: 5 },
    { nome: "Sara", nota: 8 },
    { nome: "Vinicius", nota: 6 }
];

let somaNotas = 0;
for (let i = 0; i < alunos.length; i++) {
    somaNotas += alunos[i].nota;
}

const media = somaNotas / alunos.length;
console.log("A média das notas é:", media);