arquivo = 'RAD_Python/Teste/listaMercado.txt'

def add():
    item = input('Digite o item desejado: ')
    escreve_item(item)

def escreve_item(item):
    lista = open(arquivo, 'a')
    lista.write(item+'\n')
    lista.close()


lista = ['Banana', 'Pão', 'Leite', 'Café']
with open(arquivo, 'w+', encoding='UTF-8') as compras:
    #Pulando linha
    for i in lista:
         compras.write(i+'\n')
add()
condicao = True
while condicao:
    resposta = input('Gostaria de digitar mais um item? ')
    if resposta == 'sim' or resposta == 'SIM':
        add()
    else:
        condicao = False
