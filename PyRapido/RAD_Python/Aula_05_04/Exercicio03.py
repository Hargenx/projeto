# 3.	Escreva um programa Python para verificar se a letra digitada pelo usuário do alfabeto
#  é uma vogal ou consoante.
import string
def verifica(letra):
    if letra in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        print('%s é uma vogal' %letra)
    elif letra in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'):
        print(f'{letra} é uma consoante')
    else:
        print(f'{letra} não é uma letra')
    
letra = input('Digite uma letra: ')
verifica(letra)
print(string.ascii_lowercase)