def conversor_idade_humano_cao(idade_cao):
    idade_humano = -1
    if idade_cao < 0:
        idade_humano = -1
    elif idade_cao == 0:
        idade_humano = 0
    elif idade_cao == 1:
        idade_humano = 14
    elif idade_cao == 2:
        idade_humano = 22
    else:
        idade_humano = 22 + (idade_cao - 2) * 5
    return idade_humano
