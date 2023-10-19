import sqlite3

class Database:
    def __init__(self, nome_banco):
        try:
            db = Database(nome_banco)
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS escola(
                                        id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nome TEXT,
                                        nota FLOAT)''')
            self.conn.commit()
        except Exception as e:
            print("Erro na criação da tabela: ", e)

db = Database('banco.sqlite')