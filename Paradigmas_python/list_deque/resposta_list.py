#https://www.youtube.com/watch?v=eCDFA02SiIA

def solucao(array, k):
    permutacao = []
    index = 0
    while array:
        index = (index + k - 1) % len(array)
        item = array.pop(index)
        permutacao.append(item)
    return permutacao

import time
soldados = 1_000_000
arr = [s + 1 for s in range(soldados)]
k = 3
comeco = time.perf_counter()
perm = solucao(arr, k)
fim = time.perf_counter()
print(f"Permutacao: {perm}\nTempo: {fim - comeco}")