# 1.	Escreva um programa Python para calcular o comprimento de uma string além disso contar o número de caracteres em uma string, 
# use dois métodos para isso.
# Exemplo: Se colocar para contar Estacio.br e estudante.estacio.br na sequência o resultado deve ser.
# 10
# {'e': 3, 's': 2, 't': 3, 'u': 1, 'd': 1, 'a': 2, 'n': 1, '.': 2, 'c': 1, 'i': 1, 'o': 1, 'b': 1, 'r': 1}

from collections import Counter
def frequencia_char(frase1):
    try:
        dicionario = {}
        for n in frase1:
            chave = dicionario.keys()
            if n in chave:
                dicionario[n] += 1
            else:
                dicionario[n] = 1
    except TypeError as e:
        print(f'Erro na função frequencia_char: {e}')
    else:
        return dicionario

def tamanho_string(frase2):
    try:
        cont = 0
        for _ in frase2:
            cont += 1
    except TypeError as e:
        print(f'Erro na função tamanho_string: {e}')
    else:
        return cont


# 2.	Escreva um programa Python para contar a frequência das palavras em um arquivo (txt).

def contar_palavras(nome_arq):
    try:
        with open(nome_arq) as arquivo:
            return Counter(arquivo.read().split())
    except FileNotFoundError as e:
        print(f'Erro na função contar_palavras: {e}')


# 3.	Escreva um programa Python para verificar se a letra digitada pelo usuário do alfabeto é uma vogal ou consoante.

import string
def verifica_letra(letra):
    try:
        if letra in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            print("%s é uma vogal." % letra)
        elif letra == 'w':
            print("A letra w pode ser vogal ou consoante, dependendo da forma de emprego da palvra original")
        elif letra in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'):
            print("%s é uma consoante." % letra)
        else:
            print("%s não é uma letra do alfabeto." % letra)
    except TypeError as e:
        print(f'Erro na função verifica_letra: {e}')


# 4.	Escreva um programa Python para trocar letras maiúsculas e minúsculas de uma determinada string.

def muda_case_letra(frase):
    frase_mudada = ""
    for palavra in frase:
        if palavra.isupper():
            frase_mudada += palavra.lower()
        else:
            frase_mudada += palavra.upper()
    return frase_mudada


# 5.    Escreva um programa Python para remover palavras duplicadas de uma determinada string.

def lista_unica(texto):
    palavras = texto.split()
    lista = []
    for i in palavras:
        if i not in lista:
            lista.append(i)
    return ' '.join(lista)



