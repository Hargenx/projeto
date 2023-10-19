// Obtenha a nota do usuário
const nota = parseFloat(prompt("Digite sua nota:"));

// Verifique a classificação com base na nota
if (nota >= 90) {
    console.log("Sua classificação é A");
} else if (nota >= 80) {
    console.log("Sua classificação é B");
} else if (nota >= 70) {
    console.log("Sua classificação é C");
} else if (nota >= 60) {
    console.log("Sua classificação é D");
} else {
    console.log("Sua classificação é F");
}
