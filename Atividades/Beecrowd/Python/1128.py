# Work in progress

def Juntar(L1,L2):
    for a in range(len(L2)):
        if L2[a] not in L1:
            L1.append(L2[a])
    return L1

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

    usados,index = [],0
    ref = Juntar([],Graf_inter[1])
    while True:
        try:
            if ref[index] in usados: break
        except: break
        usados.append(ref[index])
        ref = Juntar(ref,Graf_inter[ref[index]])
        index += 1
    print(1 if len(ref) == Inter else 0)