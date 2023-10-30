import sqlite3

def sql_acao():
    conn = sqlite3.connect('Python_DB/Banco_de_vendas.db')
    cursor_obj = conn.cursor()

    cursor_obj.execute(
        ''' CREATE TABLE IF NOT EXISTS vendedores(
            vendedores_id INTEGER(5), 
            nome VARCHAR(30), 
            cidade VARCHAR(50), 
            comissão FLOAT(7,2)); ''')
    cursor_obj.executescript(''' INSERT INTO vendedores VALUES( 9001, 'Bruce Wayne', 'Gothan', 0.20);
                                INSERT INTO vendedores VALUES( 9002, 'Peter Parker' , 'Nova York', 0.35);
                                INSERT INTO vendedores VALUES( 9003, 'Clark Kent', 'Metropolis', 0.50);
                                INSERT INTO vendedores VALUES( 9004, 'Matt Murdock', 'Nova York', 0.25);
                                INSERT INTO vendedores VALUES( 9005, 'Karl Franz', 'Altdorf', 0.45);
                                ''')

    #--- OUTRO ARQUIVO ---#
    cursor_obj.execute('SELECT * FROM vendedores')
    linhas = cursor_obj.fetchall()
    print('----- Detalhe dos vendedores ------')
    for linha in linhas:
        print(linha)
    print('\n---- Excluindo vendedor com o ID 9003 ----\n')
    delete_id = 9003
    cursor_obj.execute('DELETE FROM vendedores WHERE vendedores_id = ?', (delete_id, ))
    conn.commit()
    cursor_obj.execute('SELECT * FROM vendedores')
    linhas = cursor_obj.fetchall()
    print('----- Detalhe dos vendedores ------')
    for linha in linhas:
        print(linha)

sql_acao()
