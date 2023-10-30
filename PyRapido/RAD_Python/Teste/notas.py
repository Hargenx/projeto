# pip install colorama
# pip install termcolor
def desenha(texto):
    print('_' * 40)
    print(texto.center(40))
    print('_' * 40)

def menu(opcoes):
    desenha('ESCOLA ANDORRA')
    op = 1
    for item in opcoes:
        print(f'\033[32m{op}\033[34m - {item}\033[34m')
        op += 1
    print('_' * 40)
    escolha = leia_numero('\033[33mDigite sua opção: \033[33m')
    return escolha

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

arquivo = 'RAD_Python/Teste/listaNota.txt'

def arquivo_existe(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
    except Exception as ex:
        print('ERRO: Não foi possivel criar o arquivo.', ex)
    else:
        print(f'Arquivo {nome} foi criado com sucesso.')
    finally:
        arquivo.close()

def ler_arquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except FileNotFoundError as e:
        print(f'ERRO: Arquivo não encontrado.\n{e}')
    except Exception as ex:
        print('ERRO: Não foi possivel ler o arquivo.', ex)
    else:
        desenha('CADASTROS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            if float(dado[1]) < 6:
                print(f'\033[1;31mNome: {dado[0]} - Nota: {dado[1]}\033[0;0m')
            else:
                print(f'\033[1;32mNome: {dado[0]} - Nota: {dado[1]}\033[0;0m')
    finally:
        arquivo.close()

def cadastro(arquivo, nome, nota):
    try:
        arquivo = open(arquivo, 'at')
    except Exception as ex:
        print('Erro: ', ex)
    else:
        try:
            arquivo.write(f'{nome};{nota}\n')
        except Exception as ex:
            print('Erro: Não foi possivel inserir estudante', ex)
        else:
            print(f'Estudante {nome} cadastrado com sucesso, com a nota {nota}.')
        finally:
            arquivo.close()


def menu_principal():
    while True:
        opcao = menu(['Ler arquivo', 'Cadastrar Aluno', 'Sair'])
        match opcao:
            case 1:
                ler_arquivo(arquivo)
            case 2:
                nome = str(input('Nome: '))
                nota = float(input('Nota: '))
                if nota < 0:
                    print('Nota inválida, nota deve ser maior que 0.')
                elif nota > 10:
                    print('Nota inválida, nota não pode ser maior que 10.')
                else:
                    cadastro(arquivo, nome, nota)
            case 3:
                print('Até mais!')
                break
            case _:
                print('\033[31mERRO: Opção inválida.\033[m')
        
        


if __name__ == "__main__":
    menu_principal()