# Work in progress

def bfs(grafo, vertice_fonte):
    visitados, fila = set(), [vertice_fonte]
    while fila:
        vertice = fila.pop(0)
        if vertice not in visitados:
            visitados.add(vertice)
            fila.extend(set(grafo[vertice]) - set(visitados))
    return visitados

while True:
    N,M = list(map(int,input().split(" ")))
    if (N == 0) and (M == 0): break
    nodos = list([] for a in range (0, N))
    for b in range(M):
        V,W,P = list(map(int,input().split(" ")))
        nodos[V-1].append(W-1)
        if P == 2: nodos[W-1].append(V-1)
    
    Teste = True
    for c in range(N):
        if len(bfs(nodos,c)) != N:
            Teste = False
            break
    print(1 if Teste else 0)