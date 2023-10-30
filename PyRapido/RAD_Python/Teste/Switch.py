def number_to_string(valor):
    match valor:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"


if __name__ == "__main__":
    valor = input(int('Digite um numero: '))
    number_to_string(valor)
