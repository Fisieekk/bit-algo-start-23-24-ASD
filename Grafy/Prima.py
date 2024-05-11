# złożoność to O(E*logV)
import heapq

def prima(G, s = 0) :
    V = len(G)
    Q = [(0,s)]
    parents = [None] * V
    mins = [float('inf')] * V
    mins[s] = 0
    visited = [False] * V
    counter = 0
    
    # sprawdzamy ile wierzchołków już odwiedziliśmy
    while counter < V :
        # pobieramy numer wierzchołka z kolejki
        v = heapq.heappop(Q)[1]
        # jeśli wierzchołek został już odwiedzony, to go ignorujemy
        if visited[v] : continue
        # sprawdzamy wszystkich sąsiadów wierzchołka v
        for n, val in G[v] :
            # jeśli wierzchołek został już odwiedzony, to go ignorujemy
            if visited[n] : continue
            # sprawdzamy, czy dotarcie do n krawędzią (v, n) jest korzystniejsze niż poprzednia metoda
            if mins[n] > val :
                mins[n] = val
                # ustawiamy parenta n na v, co odpowiada za strukturę drzewa
                parents[n] = v
                # wrzucamy wierzchołek którego dane zmieniliśmy do kolejki
                heapq.heappush(Q, (val, n))
        # uznajemy wierzchołek v za odwiedzony i dodajemy 1 do liczby odwiedzonych wierzchołków
        visited[v] = True
        counter += 1
        
    return parents

test = [[(1,8), (2, 5)], [(0, 8), (3, 3)], [(0, 5), (3, 2), (4, 6)], [(1, 3), (2, 2), (4, 9)], [(2, 6), (3, 9)]]

print(prima(test, s = 2))