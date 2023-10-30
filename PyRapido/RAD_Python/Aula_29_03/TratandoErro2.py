def divisao():
    lista = [-1, 0, 1]
    for i in lista:
        if i == 0:
            raise ZeroDivisionError('Não é possível dividir por 0')

try:
    divisao()
except ZeroDivisionError as e:
    print(e)
