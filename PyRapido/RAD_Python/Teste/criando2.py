def leia_numero(num):
    while True:
        try:
            numero = int(input(num))
        except (ValueError, TypeError):
            print('\n\033[31mERRO: Digite um número inteiro válido. \033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mERRO: Digite um número inteiro válido. \033[m')
            return 0
        else:
            return numero

try: 
    while True: 
        n = leia_numero('Digite um número: ')
        print('- - - - '* 5)
        print('[1] Binário')
        print('[2] Octal')
        print('[3] Hexadecimal')
        print('[x] Sair')
        opcao = str(input('Digite a opção que deseja converter: '))
        match opcao:
            case '1':
                print('{0:b}'.format(n))
                print(f'O número {n} em binário é {n:b}')
                binario = str(bin(n))
                print(binario)
            case '2':
                print('{0:o}'.format(n))
                print(f'O número {n} em octal é {n:o}')
                octa = str(oct(n))
                print(octa)
            case '3':
                print('{0:x}'.format(n))
                print(f'O número {n} em hexadecimal é {n:x}')
                hexa = str(hex(n))
                print(hexa)
            case 'x':
                print('Saindo...')
                break
            case _:
                print('Opção inválida!')
except ValueError as ve:
    print(f'Você digitou um valor inválido: {ve}')
except KeyboardInterrupt as ki:
    print(f'Você interrompeu o programa: {ki}')
    # if opcao == 'x'or opcao == 'X':
    #     break
    # elif opcao == '1' or opcao == '2' or opcao == '3':
    #     if opcao == '1':
    #         rio = str(bin(n))
    #         print(rio)
    #     elif opcao == '2':
    #         cta = str(oct(n))
    #         print(cta)

    #     elif opcao == '3':
    #         exa = str(hex(n))
    #         print(exa)

    # else:
    #     print('Opção invalida!')