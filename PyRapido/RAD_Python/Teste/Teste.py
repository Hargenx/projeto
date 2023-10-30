


arquivo = open("RAD_Python/Teste/nomes.txt", "w")
arquivo.write('Raphael\'s')
arquivo.close()

arquivo = open('RAD_Python/Teste/nomes.txt', 'r')
print(arquivo.readline())
arquivo.close()


with open('RAD_Python/Teste/nomes.txt', 'r') as arquivo:
    print(arquivo.readline())

import os
os.remove('RAD_Python/Teste/nomes.txt')

