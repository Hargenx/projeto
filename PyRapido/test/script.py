try:
    entrada = float(input('Digite seu tamanho: '))
except Exception as e:
    print(f'Tipo errado: {e}')
else:
    print(f'Você tem {entrada}m!')
finally:
    print('🦉')


import sqlite3
def banco():
    try:
        db = "escola.db"
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS escola(
                                id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT,
                                nota FLOAT)''')
        conn.commit()
    except Exception as e:
        print("Erro na criação da tabela: ", e)
banco()


