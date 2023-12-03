#https://www.youtube.com/watch?v=eCDFA02SiIA
from collections import deque
def solucao(array, k):
    d = deque(array)
    permutacao = []
    while d:
        d.rotate(1 - k)
        item = d.popleft()
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