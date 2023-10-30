#4.	Escreva um programa Python para trocar letras maiúsculas e minúsculas de uma determinada string.

def muda_letra(frase):
    try:
        frase_mudada = ''
        for letra in frase:
            if letra.isupper():
                frase_mudada += letra.lower()
            else:
                frase_mudada += letra.upper()
    except KeyError as erro:
        print(f'Erro: {erro}')
    else:
        return frase_mudada

print(muda_letra('Python, JAVA, C++'))

texto = 'Python, JAVA, C++'
print(texto.swapcase())