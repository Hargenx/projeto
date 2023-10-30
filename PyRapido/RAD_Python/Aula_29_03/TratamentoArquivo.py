import os
try:
    arquivo = os.scandir('RAD_Python/Aula_29_03')
    for arquivos in arquivo:
        print(arquivos)
        print('--------------------------------')
        print(f'Nome do documento: {arquivos.name}')
        print(f'Nome do diretório: {arquivos.path}')
        print(f'Tamanho do arquivo: {arquivos.stat().st_size}')
        print(f'proprietário: {arquivos.stat().st_uid}')
        print(f'grupo: {arquivos.stat().st_gid}')
        print('--------------------------------')
except FileNotFoundError as erro:
    print(f'Arquivo não encontrado: {erro}')
except PermissionError as erro:
    print(f'Permissão negada: {erro}')
except Exception as e:
    print(f'Erro: {e}')