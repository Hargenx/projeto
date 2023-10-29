from banco import banco
from model import Jogo

# Conectar-se ao banco de dados SQLite
conn = banco()
cursor = conn.cursor()

class JogoController:
    def criar_jogo(self, nome, genero, plataforma, lancamento):
        cursor.execute('''
        INSERT INTO jogos (nome, genero, plataforma, lancamento)
        VALUES (?, ?, ?, ?)
        ''', (nome, genero, plataforma, lancamento))
        conn.commit()

    def listar_jogos(self):
        cursor.execute('SELECT * FROM jogos')
        rows = cursor.fetchall()
        jogos = [Jogo(*row) for row in rows]
        return jogos

    def atualizar_jogo(self, jogo):
        cursor.execute('''
        UPDATE jogos
        SET nome=?, genero=?, plataforma=?, lancamento=?
        WHERE id=?
        ''', (jogo.nome, jogo.genero, jogo.plataforma, jogo.lancamento, jogo.id))
        conn.commit()

    def deletar_jogo(self, jogo_id):
        cursor.execute('DELETE FROM jogos WHERE id=?', (jogo_id,))
        conn.commit()
