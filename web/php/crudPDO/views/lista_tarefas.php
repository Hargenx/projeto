<!DOCTYPE html>
<html>
<head>
    <title>Lista de Tarefas</title>
</head>
<body>
    <h1>Lista de Tarefas</h1>
    <ul>
        <?php foreach ($tarefas as $tarefa): ?>
            <li>
                <?php echo $tarefa->getTitulo(); ?>
                <a href="index.php?action=delete&id=<?php echo $tarefa->getId(); ?>">Excluir</a>
            </li>
        <?php endforeach; ?>
    </ul>
    <form action="index.php" method="post">
        <input type="text" name="nova_tarefa" placeholder="Nova Tarefa" required>
        <button type="submit">Adicionar Tarefa</button>
    </form>
</body>
</html>
