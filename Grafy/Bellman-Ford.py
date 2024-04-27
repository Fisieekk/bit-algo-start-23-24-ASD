#  złożoność to O(VE)
def bellman_ford(G, s) :
    V = len(G)
    distances = [float('inf')]*V
    distances[s] = 0
    
    # główna pętla programu - V-1 relaksacji krawędzi
    for _ in range(V - 1) :
        # wybór krawędzi
        for v in range(V) :
            for u,val in G[v] :
                # relaksacja (czy do u da się dostać wydajniej przez v)
                value = distances[v] + val
                if distances[u] > value :
                    distances[u] = value
                    
    # sprawdzenie istnienia cykli ujemnych
    # wybór krawędzi
    for v in range(V) :
        for u,val in G[v] :
            # sprawdzenie czy do u da się dostać wydajniej przez v -> jeśli tak, to znaczy że (v,u) leży w cyklu ujemnym
            if distances[u] > distances[v] + val :
                return False
            
    return distances


graph = [[(2,-1)],[(0,-1)],[(1,1)]]

print(bellman_ford(graph,0))