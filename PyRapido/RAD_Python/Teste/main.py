if __name__ == '__main__':
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    from cachorroHomem import conversor_idade_humano_cao as converte
    idade = float(input("Qual a idade do seu cachorro: "))
    print("A idade do seu cachorro: ", float(converte(idade)))
