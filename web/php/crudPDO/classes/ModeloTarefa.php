<?php
require_once 'config.php';

class ModeloTarefa {
    public function getTarefas() {
        $tarefas = [];

        try {
            $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            $query = "SELECT id, titulo FROM tarefas";
            $stmt = $pdo->prepare($query);
            $stmt->execute();

            while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                $tarefa = new Tarefa($row['id'], $row['titulo']);
                $tarefas[] = $tarefa;
            }
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }

        return $tarefas;
    }

    public function criarTarefa($titulo) {
        try {
            $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            $query = "INSERT INTO tarefas (titulo) VALUES (:titulo)";
            $stmt = $pdo->prepare($query);
            $stmt->bindParam(':titulo', $titulo, PDO::PARAM_STR);
            $stmt->execute();
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }

    public function excluirTarefa($id) {
        try {
            $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            $query = "DELETE FROM tarefas WHERE id = :id";
            $stmt = $pdo->prepare($query);
            $stmt->bindParam(':id', $id, PDO::PARAM_INT);
            $stmt->execute();
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }

    public function getTarefaPorId($id) {
        // Implementar a recuperação de uma tarefa pelo ID.
    }
}
