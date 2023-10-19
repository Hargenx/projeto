const alunos = [
    { nome: "Raphael", nota: 7 },
    { nome: "Caroline", nota: 9 },
    { nome: "Gilson", nota: 5 },
    { nome: "Sara", nota: 8 },
    { nome: "Vinicius", nota: 6 }
];

function adicionarAluno() {
    const nome = document.getElementById("nome").value;
    const nota = document.getElementById("nota").valueAsNumber;
    if (nome && nota) {
        const aluno = { nome, nota };
        alunos.push(aluno);
        atualizarTabela();
    }
}
function atualizarTabela() {
    const tabelaNotas = document.getElementById("tabela-notas");
    tabelaNotas.innerHTML = "";
    for (let i = 0; i < alunos.length; i++) {
        const tr = document.createElement("tr");
        const tdNome = document.createElement("td");
        const tdNota = document.createElement("td");
        tdNome.innerText = alunos[i].nome;
        tdNota.innerText = alunos[i].nota;
        tr.appendChild(tdNome);
        tr.appendChild(tdNota);
        tabelaNotas.appendChild(tr);
    }
}
