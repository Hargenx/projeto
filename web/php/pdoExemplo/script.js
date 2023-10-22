document.addEventListener("DOMContentLoaded", function () {
    // Elementos HTML
    const taskForm = document.getElementById("task-form");
    const novaTarefaInput = document.getElementById("nova_tarefa");
    const tarefasLista = document.getElementById("tarefas-lista");
    const modalConfirmacao = document.getElementById("modal-confirmacao");
    const confirmarExclusaoBtn = document.getElementById("confirmar-exclusao");
    const cancelarExclusaoBtn = document.getElementById("cancelar-exclusao");

    // Função para criar um elemento de lista de tarefas
    function criarTarefaElement(tarefa) {
        const li = document.createElement("li");
        li.innerHTML = `${tarefa.titulo} <button data-id="${tarefa.id}" class="excluir-tarefa">Excluir</button>`;
        return li;
    }

    // Função para atualizar a lista de tarefas
    function atualizarListaTarefas() {
        tarefasLista.innerHTML = ""; // Limpa a lista
        // Aqui, você pode buscar as tarefas do servidor com AJAX ou adicionar manualmente
        // Exemplo manual:
        const tarefaExemplo = { id: 1, titulo: "Exemplo de tarefa" };
        tarefasLista.appendChild(criarTarefaElement(tarefaExemplo));
        // Fim do exemplo manual
    }

    // Evento de envio do formulário
    taskForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const novoTituloTarefa = novaTarefaInput.value;

        // Aqui, você pode enviar a nova tarefa para o servidor com AJAX
        // Após a inserção, você pode atualizar a lista de tarefas com a função atualizarListaTarefas
        // Exemplo manual:
        const tarefaExemplo = { id: 2, titulo: novoTituloTarefa };
        tarefasLista.appendChild(criarTarefaElement(tarefaExemplo));
        novaTarefaInput.value = ""; // Limpa o campo
        // Fim do exemplo manual
    });

    // Evento de clique em um botão de exclusão de tarefa
    tarefasLista.addEventListener("click", function (e) {
        if (e.target.classList.contains("excluir-tarefa")) {
            const tarefaId = e.target.getAttribute("data-id");

            // Exibir o modal de confirmação
            modalConfirmacao.style.display = "block";

            // Evento de clique no botão "Sim" do modal
            confirmarExclusaoBtn.onclick = function () {
                modalConfirmacao.style.display = "none";
                // Aqui, você pode enviar a solicitação de exclusão da tarefa ao servidor com AJAX
                // Após a exclusão, você pode atualizar a lista de tarefas com a função atualizarListaTarefas
                // Exemplo manual:
                e.target.parentElement.remove(); // Remove a tarefa da lista
                // Fim do exemplo manual
            };

            // Evento de clique no botão "Cancelar" do modal
            cancelarExclusaoBtn.onclick = function () {
                modalConfirmacao.style.display = "none";
            };
        }
    });

    // Inicializa a lista de tarefas
    atualizarListaTarefas();
});
