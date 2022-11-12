T = int(input())
for a in range(T):
  if a != 0:
    print("")
  Dic,lc = {},[]
  N,L = list(map(int,input().split(" ")))
  for e in range(L):
    p,l,c,v = list(map(int,input().split(" ")))
    if (l,c) in lc:
      Dic[(l,c)] += v
    else:
      lc.append((l,c))
      Dic[(l,c)] = v
  lc.sort(key=lambda x:(x[0],x[1]))
  for i in lc:
    print(i[0],i[1],Dic[i])
