import sqlite3

class Database:
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.create_table()
        except sqlite3.Error as e:
            print("Erro na conexão com o banco de dados:", e)

    def create_table(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS escola (
                    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    nota FLOAT
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print("Erro na criação da tabela: ", e)

    def close(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print("Erro ao fechar a conexão com o banco de dados:", e)

# Exemplo de uso:
if __name__ == "__main__":
    try:
        db = Database("escola.db")
        # Agora você pode usar db para interagir com o banco de dados.
        # Por exemplo, inserir dados:
        db.cursor.execute("INSERT INTO escola (nome, nota) VALUES (?, ?)", ("Alice", 9.5))
        db.cursor.execute("INSERT INTO escola (nome, nota) VALUES (?, ?)", ("Bob", 8.0))
        db.conn.commit()

        # Consultar dados:
        db.cursor.execute("SELECT * FROM escola")
        rows = db.cursor.fetchall()
        for row in rows:
            print(row)

        # Fechar a conexão com o banco de dados quando terminar
        db.close()
    except Exception as e:
        print("Erro geral:", e)
