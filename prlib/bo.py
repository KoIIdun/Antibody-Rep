from random import randint as rnd
from scipy.sparse import dok_matrix

def bak_ost(V, K, a):
    graph = dok_matrix((V // K, V // K))
    numbers = [0] * (V // K)
    graph[0, 0] = 1
    vertex = [1] + [0] * (n - 1)
    for i in range(1, V):
        denominator = rnd(1, (a + 1) * (i + 1) - 1)
        if denominator <= a:
            j = i
        else:
            mark = True
            for i in range(0, i):
                denominator = rnd(1, (a + 1) * (i + 1) - 1)
                if denominator <= vertex[i] - 1 + a:
                    j = i
                    mark = False
            if mark:
                j = i - 1 
        vertex[j] += 1
        graph[j // K, i // K] += 1
        numbers[j // K] += 1
        for i in graph.keys():
                graph[i[0], i[1]] /= numbers[i[0]]        
    return graph