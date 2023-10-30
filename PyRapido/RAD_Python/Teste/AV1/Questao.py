arquivo = './RAD_Python/Teste/AV1/lista.txt'
with open(arquivo, 'w') as agenda:
    dado = input('Digite o nome: ')
    agenda.write(dado + '\n')
with open(arquivo, 'r') as agenda:
    for nomes in agenda:
        print(nomes, end='')
