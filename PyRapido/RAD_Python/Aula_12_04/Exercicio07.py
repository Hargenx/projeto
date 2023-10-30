# A
#Criando Tupla
tupla = ()
print(tupla)
#Criando uma tupla vazia utiliznado tuple() uma função function built-in Python
tupla2 = tuple()
print(tupla2)

# B
numeros = {0: 10, 1: 20}
print(numeros)
numeros.update({2: 30})
print(numeros)

#C
def somar_lista(itens):
    soma_numeros = 0
    for i in itens:
        soma_numeros += i
    return soma_numeros


if __name__ == "__main__":
    print(somar_lista([2, 1, -8, 2.4, 3.6]))
