''' Jako bankier masz dostęp do kursów wymiany walut. Chcesz znaleźć taki sposób wymiany pieniędzy (które posiadasz w konkretnej walucie), żeby zarobić jak najwięcej tylko poprzez wymianę walutową '''



def bellman_ford(G, s) :
    V = len(G)
    costs = [float('-inf')] * V
    costs[s] = 1
    parent = [None] * V
    
    for _ in range(V - 1) :
        for v in range(V) :
            for u,val in G[v] :
                value = costs[v] / val
                if costs[u] < value :
                    costs[u] = value
                    parent[u] = v
           
    path = None
                    
    if costs[s] > 1 :
        path = [s]
        current = s
        
        while len(path) <= 1 or current != s :
            current = parent[current]
            path.append(current)
        path.reverse()
            
    return path


graph = [[(1,0.98)],[(2,0.98)],[(0,0.98)]]

print(bellman_ford(graph,0))