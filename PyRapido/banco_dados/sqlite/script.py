import sqlite3
from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    nota: float
    id_aluno: int = None
class Database:
    def __init__(self, nome_banco):
        try:
            self.conn = sqlite3.connect(nome_banco)
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

    def insert_aluno(self, aluno: Aluno):
        try:
            self.cursor.execute("INSERT INTO escola (nome, nota) VALUES (?, ?)", (aluno.nome, aluno.nota))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Erro ao inserir aluno:", e)

    def get_alunos(self):
        try:
            self.cursor.execute("SELECT * FROM escola")
            rows = self.cursor.fetchall()
            alunos = [Aluno(id_aluno=row[0], nome=row[1], nota=row[2]) for row in rows]
            return alunos
        except sqlite3.Error as e:
            print("Erro ao buscar alunos:", e)

# Exemplo de uso:
if __name__ == "__main__":
    try:
        db = Database("escola.sqlite")
        db.insert_aluno(Aluno(nome="Alice", nota=9.5))
        db.insert_aluno(Aluno(nome="Bob", nota=8.0))

        alunos = db.get_alunos()
        for aluno in alunos:
            print(aluno)

        db.close()
    except Exception as e:
        print("Erro geral:", e)
