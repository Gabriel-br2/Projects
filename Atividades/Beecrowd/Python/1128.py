# Work in progress

while True:
    Graf_inter = {}
    Graf_nodo = []
    Inter,Rua = list(map(int,input().split(" ")))
    if Inter == 0 and Rua == 0: break
    for a in range(Rua):
        V,W,P = list(map(int,input().split(" ")))
        if V not in Graf_nodo:
            Graf_nodo.append(V)
            Graf_inter[V] = [W]
        else: Graf_inter[V].append(W)
        if P == 2: 
            if W not in Graf_nodo: 
                Graf_nodo.append(W)
                Graf_inter[W] = [V]
            else: Graf_inter[W].append(V)
    print(Graf_inter) 