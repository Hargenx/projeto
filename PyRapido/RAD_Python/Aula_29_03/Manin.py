import os
try:
    os.system('cls' if os.name == 'nt' else 'clear')
    from cachorroHomem import conversor_idade_humano_cao as converte
    idade = float(input('Qual a idade do cachorro? '))
    print(f'A idade do cachorro em humanos é {converte(idade)} anos.')
except ValueError as e:
    print(f'Erro: {e}')
except Exception as e:
    print(f'Erro: {e}')