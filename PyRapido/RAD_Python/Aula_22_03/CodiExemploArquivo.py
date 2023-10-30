arquivo = open("RAD_Python/Aula_22_03/nomes.txt", "a")
arquivo.write('\nRaphael\'s')
arquivo.close()

arquivo = open('RAD_Python/Aula_22_03/nomes.txt', 'r')
print(arquivo.readlines())
arquivo.close()