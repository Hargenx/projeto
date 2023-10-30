#2.	Escreva um programa Python para contar a frequência das palavras em um arquivo(txt).
from collections import Counter
def contar_palavras(nome_arquivo):
    try:
        with open(nome_arquivo) as arquivo:
            return Counter(arquivo.read().split())
    except FileNotFoundError as erro:
        print(f'Erro: {erro}')


print('Numero de palavras no arquivo: ', contar_palavras('RAD_Python/Aula_05_04/Palavras.txt'))
