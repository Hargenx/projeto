import Exercicio_summa as es


print(es.tamanho_string("Estacio.br"))
print(es.frequencia_char("estudante.estacio.br"))

print("\nNumero de palavras no arquivo: ", es.contar_palavras("RAD_Python/Teste/Testando_Exercicio/Exer05_04/palavras.txt"))
# Colocar outra solução.
arquivo = open('RAD_Python/Teste/Testando_Exercicio/Exer05_04/palavras.txt')
# Usando dict() já vindo do Python, um dicionario já automatico.
contagem = []
for linhas in arquivo:
    palavras = linhas.split()
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
print(f'Numero de palavras no arquivo: {contagem}')


es.verifica_letra(letra=input("Digite a letra: "))
print(es.string.ascii_uppercase)


print(es.muda_case_letra("Pytho E JAVA"))

texto = 'Estacio de Sa'
print(texto.swapcase())

texto = "Python Java Java JavaScript C PHP Python c"
print("Texto original: ", texto)
print("Texto sem duplicatas: ", es.lista_unica(texto))
