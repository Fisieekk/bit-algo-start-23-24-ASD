'''Polecenie: Wieszchołek v w grafie skierowanym nazywamy dobrym poczatkiem, jezeli każdy inny wieszchołek mozna osiągnąć scieżką skierowaną wychodzącą z v
Stwórz algorytm, który dla podanego grafu stwierdza czy G posiada dobry poczatek; lista sąsiedztwa, złożonośc O(V+E)'''

def poczatek(G):
    #dfs
    def DFSvisit(i):
        nonlocal G, times, time, visited
        visited[i] = True
        for v in G[i]:
            if not visited[v]:
                DFSvisit(v)
        #czas WYJŚCIA NIE WEJŚCIA!!!!!
        time += 1
        times[i] = time

    n = len(G)
    times = [-1 for _ in range(n)]
    time = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            DFSvisit(i)
    #znajdowanie ostatniego wieszchołka wyjścia 
    #(skoro jest ich n będzie miał wartość wyjścia na), 
    #on będzie naszym potencjalnym dobrym początkiem (jak nie on to żaden inny też nie może być) 
    for i in range(n):
        if times[i] == n:
            s = i
            break

    #visited = [False for _ in range(n)] #sprawdzenie czy wszystkie są visited
    time = 0 #sprawdzenie czy time jest równe n, co jest adekwatne 
             #do tego że wszyscy zostali odwiedzeni
    DFSvisit(s)
    return time == n #return !(False in visited)