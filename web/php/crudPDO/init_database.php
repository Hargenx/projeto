<?php
// Configurações do banco de dados
$hostname = 'localhost'; // Hostname do servidor MySQL
$username = 'root'; // Nome de usuário do MySQL
$password = 'root'; // Senha do MySQL
$database = 'aula_pdo'; // Nome do banco de dados

// Conexão com o servidor MySQL
$mysqli = new mysqli($hostname, $username, $password);

// Verifica se a conexão foi bem-sucedida
if ($mysqli->connect_error) {
    die("Erro na conexão: " . $mysqli->connect_error);
}

// Cria o banco de dados
$createDatabaseSQL = "CREATE DATABASE IF NOT EXISTS $database";
if ($mysqli->query($createDatabaseSQL) === true) {
    echo "Banco de dados criado com sucesso.<br>";
} else {
    die("Erro ao criar o banco de dados: " . $mysqli->error);
}

// Seleciona o banco de dados
$mysqli->select_db($database);

// Cria a tabela de tarefas
$createTableSQL = "CREATE TABLE IF NOT EXISTS tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL
)";
if ($mysqli->query($createTableSQL) === true) {
    echo "Tabela de tarefas criada com sucesso.<br>";
} else {
    die("Erro ao criar a tabela de tarefas: " . $mysqli->error);
}

// Fecha a conexão com o banco de dados
$mysqli->close();
?>