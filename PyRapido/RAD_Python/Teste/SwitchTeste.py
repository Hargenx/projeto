from email.policy import default


def number_to_string(valor):
    match valor:
        case 0:
            print('Zero')
        case 1:
            print('Um')
        case 2:
            print('Dois')
        case _:
            print(f'Não é número valido, você digitou {format(valor)} e so é aceito de 0 a 2')


if __name__ == "__main__":
    valor = int(input('Digite um numero: '))
    number_to_string(valor)
