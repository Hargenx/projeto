def lendo_arquivo(arquivo):
    try:
        with open(arquivo, "w+") as arquivos:
            arquivos.write("Python\n")
            arquivos.write("Java")
    except FileNotFoundError as e:
        print(f"Arquivo não encontrado{e}")
    try:
        txt = open(arquivo)
        print(txt.read())
    except FileNotFoundError as e:
        print(f"Arquivo não encontrado{e}")
    finally:
        txt.close()


if __name__ == "__main__":
    lendo_arquivo('/Arquivo.txt')


