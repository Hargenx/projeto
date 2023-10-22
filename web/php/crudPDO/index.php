<?php
require 'init_database.php';
require_once 'config.php';
require_once 'classes/Tarefa.php';
require_once 'classes/ModeloTarefa.php';

$modeloTarefa = new ModeloTarefa();
$tarefas = $modeloTarefa->getTarefas();
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['nova_tarefa'])) {
    $novoTituloTarefa = $_POST['nova_tarefa'];
    $modeloTarefa->criarTarefa($novoTituloTarefa);
}

if (isset($_GET['action']) && $_GET['action'] === 'delete' && isset($_GET['id'])) {
    $tarefaId = $_GET['id'];
    $modeloTarefa->excluirTarefa($tarefaId);
}

include 'views/lista_tarefas.php';
