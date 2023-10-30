with open('RAD_Python/Aula_22_03/dados.txt', 'w') as dados:
    dados.write('Texto...')
    dados.write('\nTexto pulando linha...')
    linhas = ['Linha 2\nlinha 3\n', 'Linha 4\n', 'Linha 5']
    dados.writelines(linhas)

import os
os.remove('RAD_Python/Aula_22_03/dados.txt')

