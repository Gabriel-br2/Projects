while True:
    a = int(input())
    if a == 0: break
    d = list(map(int,input().split(" ")))
    t = 0
    for c in range(1,a):
        if(d[c-1]<0): t = t + (-1)*d[c-1]
        else: t += d[c-1]
        d[c] += d[c-1] 
    print(t)