while True:
    try:
        N = int(input())
        A = []
        for a in range(0,N):
            A.append([])
            for e in range(0,N):
                A[a].append("3")
            C = N - 1
        for a in range(0,N):
            A[a][a] = "1"
            A[a][C] = "2"
            C = C - 1
            F = "".join(A[a])
            print(F)
    except EOFError:
        break