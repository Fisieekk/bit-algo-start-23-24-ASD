#import
from collections import deque

'''Polecenie: sprawdź czy graf jest dwudzielny'''

#alternatywne rozwiązanie było na wykładzie

#G -> lista sąsiedztwa
def dwudzielnosc(G):
    #ilość wieszchołków
    n = len(G)
    #ustawiamy tablice kolorów (kolorowanie kolorami 0 i 1)
    colors = [-1 for _ in range(n)]
    #kolejka
    Q = deque()
    #wartości wstępne
    Q.append(0)
    colors[0] = 0
    #BFS
    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            #zamiast visited możemy od razu użyć colors
            if colors[v] == -1: 
                colors[v] = (colors[u] + 1) % 2
                Q.append(v)
            #jeżeli wieszchołek byłby tego samego koloru, 
            #nie jesteśmy w stanie pokolorować 2 kolorami - nie jest dwudzielny
            elif colors[v] == colors[u]:
                return False
    return True