N = int(input())
for a in range(N):
  P,D = [],0
  L = list(input())
  for e in range(len(L)):
    if L[e] == '<':
      P.append(L[e])
    elif L[e] == '>' and e != 0:
      if len(P) != 0:
        P.pop()
        D += 1
  print(D)