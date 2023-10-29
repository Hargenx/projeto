import sqlite3
import os

# Obtenha o diretório atual do arquivo banco.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho para o banco de dados na mesma pasta
DB_PATH = os.path.join(current_dir, 'jogos.db')

def banco():
    # Conectar-se ao banco de dados SQLite
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Criar tabela para armazenar os jogos
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS jogos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        genero TEXT,
        plataforma TEXT,
        lancamento INTEGER
    )
    """
    )

    conn.commit()
    return conn
