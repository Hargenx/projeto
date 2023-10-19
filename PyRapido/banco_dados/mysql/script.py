import mysql.connector

# Conectando ao banco de dados MySQL
conn = mysql.connector.connect(
    user='seu_usuario',
    password='sua_senha',
    host='seu_host',
    database='seu_banco_de_dados'
)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        idade INT
    )
''')

cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (%s, %s)", ('Raphael', 38))

cursor.execute("UPDATE usuarios SET idade = %s WHERE nome = %s", (39, 'Raphael'))
cursor.execute('SELECT * FROM usuarios')
dados = cursor.fetchall()
cursor.execute("DELETE FROM usuarios WHERE nome = %s", ('Raphael',))
cursor.execute('SELECT nome, idade FROM usuarios WHERE idade > %s', (25,))
