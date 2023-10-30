import string

def letras_documento(numero):
    try:
        with open("RAD_Python/Aula_12_04/alfabeto.txt", "w") as arquivo:
            alfabeto = string.ascii_uppercase
            letras = [alfabeto[i:i + numero] + "\n" for i in range(0, len(alfabeto), numero)]
            arquivo.writelines(letras)
    except FileNotFoundError as e:
        print(f"Arquivo não encontrado{e}")

if __name__ == "__main__":
    letras_documento(3)
