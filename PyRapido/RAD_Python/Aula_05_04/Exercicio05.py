# 5.	Escreva um programa Python para remover palavras duplicadas de uma determinada string.
def lista_unica(texto):
    try:
        lista = texto.split()
        lista_unica = []
        for palavra in lista:
            if palavra not in lista_unica:
                lista_unica.append(palavra)
    except KeyError as erro:
        print(f'Erro: {erro}')
    else:
        return ' '.join(lista_unica)

texto = "Python, JAVA, C++, JAVA, C++, JAVA, C++, PHP, JavaScript, PHP, Python, Lua"
print(lista_unica(texto))