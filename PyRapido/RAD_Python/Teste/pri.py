texto = ('Nossa aula manipulado String')
print(texto.find('aula'))
texto = (texto.replace('aula', 'A'))
print(texto)

nome = str(input('Digite seu nome: '))
print('Seu nome é {}'.format(nome))
print('Seu nome tem {} letras'.format(len(nome)))
print(nome.rstrip())


print(' '.join(texto))
print(texto.split())
print(' '.join(texto.split()))