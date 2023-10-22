<?php
require_once 'config.php';

// Função para criar a tabela de tarefas se não existir
function criarTabelaTarefas(PDO $pdo) {
    $createTableSQL = "CREATE TABLE IF NOT EXISTS tarefas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL
    )";

    try {
        $pdo->exec($createTableSQL);
    } catch (PDOException $e) {
        die("Erro ao criar a tabela de tarefas: " . $e->getMessage());
    }
}

// Verifica se há uma ação de exclusão
if (isset($_GET['action']) && $_GET['action'] === 'delete' && isset($_GET['id'])) {
    // Lógica de exclusão
    $tarefaId = $_GET['id'];

    // Exibir o modal de confirmação no JavaScript
    echo "<script>exibirModalExclusao($tarefaId);</script>";

    // Para interromper a execução do restante da página
    die();
}

$tarefas = [];

// Recupere as tarefas do banco de dados
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Crie a tabela de tarefas se ela não existir
    criarTabelaTarefas($pdo);

    $stmt = $pdo->query("SELECT * FROM tarefas");
    $tarefas = $stmt->fetchAll(PDO::FETCH_ASSOC);

} catch (PDOException $e) {
    die("Erro ao conectar ou buscar dados do banco de dados: " . $e->getMessage());
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Lista de Tarefas</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Lista de Tarefas</h1>
        <form id="task-form" action="index.php" method="POST">
            <input type="text" id="nova_tarefa" name="nova_tarefa" placeholder="Adicionar nova tarefa" required>
            <button type="submit">Adicionar</button>
        </form>
        <ul id="tarefas-lista">
            <?php foreach ($tarefas as $tarefa) : ?>
                <li>
                    <?php echo $tarefa['titulo']; ?>
                    <button data-id="<?php echo $tarefa['id']; ?>" class="excluir-tarefa">Excluir</button>
                </li>
            <?php endforeach; ?>
        </ul>
    </div>

    <!-- Modal de confirmação de exclusão -->
    <div id="modal-confirmacao" class="modal">
        <div class="modal-content">
            <h2>Confirmar Exclusão</h2>
            <p>Tem certeza de que deseja excluir esta tarefa?</p>
            <div class="modal-buttons">
                <button id="confirmar-exclusao">Sim</button>
                <button id="cancelar-exclusao">Cancelar</button>
            </div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
