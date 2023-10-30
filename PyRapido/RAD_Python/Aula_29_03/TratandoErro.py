try:
    lista = ['Raphael', 'Caroline', 'Vanessa']
    print(lista[3])
except IndexError as erro:
    print(f'Erro: {erro}')