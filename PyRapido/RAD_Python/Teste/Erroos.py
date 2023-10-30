if __name__ == '__main__':
    import os
    try:
        verifica = os.scandir('RAD_Python//Teste')
        for arquivo in verifica:
            print(arquivo)
            print('--------------------------------')
            print(f'Nome documento: {arquivo.name}')
            print(f'Tamanho: {arquivo.stat().st_size}')
            print(f'Data de modificação: {arquivo.stat().st_mtime}')
            print(f'Data de criação: {arquivo.stat().st_ctime}')
            print(f'Tipo: {arquivo.stat().st_mode}')
            print(f'Proprietário: {arquivo.stat().st_uid}')
            print(f'Grupo: {arquivo.stat().st_gid}')
            print(f'Permissões: {arquivo.stat().st_mode}')
            print('--------------------------------')
    except FileNotFoundError as e:
        print(f'Arquivo não encontrado: {e}')
    except PermissionError as e:
        print(f'Permissão negada: {e}')
    except Exception as e:
        print(f'Erro: {e}')
