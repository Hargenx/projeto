function publicarTabela() {
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const erro = document.getElementById('erro');
    erro.innerHTML = (!nome || !email) ? 'Nome e email é requerido.' : '';
    if (nome && email) {
        const tableElement = document.getElementById('tabela');
        const trElement = document.createElement('tr');
        const tbodyElement = document.createElement('tbody');
        const nomeEle = document.createElement('td');
        const emailEle = document.createElement('td');
        nomeEle.innerHTML = nome;
        emailEle.innerHTML = email;
        trElement.appendChild(nomeEle);
        trElement.appendChild(emailEle);
        tbodyElement.appendChild(trElement);
        tableElement.appendChild(tbodyElement);
        document.getElementById('nome').value = '';
        document.getElementById('email').value = '';
    }
}
