import sqlite3

conn = sqlite3.connect('Python_DB/agenda.sqlite')
cur = conn.cursor()

# criando a tabela
try:
    cur.execute(''' CREATE TABLE IF NOT EXISTS contato(
                            id_contato INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            sobrenome TEXT,
                            email TEXT,
                            telefone TEXT); ''')
except sqlite3.Error as e:
    print('ERRO: Falha na criação do banco.', e)

nome = str(input('Digite o nome: '))
sobrenome = str(input('Digite o sobrenome: '))
email = str(input('Digite o email: '))
telefone = str(input('Digite o telefone: '))

lista = [(nome, sobrenome, email, telefone)]

# [C]reate
cur.executemany(
    """INSERT INTO contato (nome, sobrenome, email, telefone)
        VALUES(?, ?, ?, ?)""", lista)
conn.commit()
print('Dados inseridos com sucesso!')

# [R]ead
cur.execute('SELECT * FROM contato')
for linha in cur.fetchall():
    print(linha)

# [U]pdate
id_contato = int(input('Digite o id para troca de telefone: '))
novoNumero = int(input('Digite o novo numero: '))
cur.execute('UPDATE contato SET telefone = ? WHERE id_contato = ?',(novoNumero, id_contato))

# [R]ead
cur.execute('SELECT * FROM contato')
for linha in cur.fetchall():
    print(linha)

# [D]elete
id_contato = int(input('Digite o id do contato que deseja deletar: '))
cur.execute('DELETE FROM contato WHERE id_contato = ?',
            (id_contato, ))
conn.commit()
