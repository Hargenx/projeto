# 1.	Escreva um programa Python para calcular o comprimento de uma string além disso contar o número de caracteres
#    em uma string, use dois métodos para isso.
# Exemplo: Se colocar para contar Estacio.br e estudante.estacio.br na sequência o resultado deve ser.
# 10
# {'e': 3, 's': 2, 't': 3, 'u': 1, 'd': 1, 'a': 2, 'n': 1, '.': 2, 'c': 1, 'i': 1, 'o': 1, 'b': 1, 'r': 1}

def frequencia_char(frase):
    try:
        dicionario = {}
        for letra in frase:
            chave = dicionario.keys()
            if letra in chave:
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1
    except KeyError as erro:
        print(f'Erro: {erro}')
    else:
        return dicionario

def frequencia_string(frase):
    try:
        cont = 0
        for _ in frase:
            cont += 1
    except KeyError as erro:
        print(f'Erro: {erro}')
    else:
        return cont


print(len('Estacio.br'))
print(frequencia_string('Estacio.br'))
print(frequencia_char('estudante.estacio.br'))
