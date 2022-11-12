import math as mt
F = []
while True:
	N,M = list(map(int,input().rstrip().split()))
	F.append((N,M))
	if N == 0 and M == 0:
		break
	L = []
	for a in range(N):
		PI = 0
		En = int(input())
		if En % 2 == 0:
			PI = 2
		else:
			PI = 1
		L.append((En,int(mt.fmod(En,M)),PI))
	L.sort(key=lambda x: (x[1],x[2],x[0] if x[2] == 2 else -x[0]))
	F.append(L)
for e in range(len(F)):
	if len(F[e]) == 2:
		print(F[e][0],F[e][1])
	else:
		for i in range(len(F[e])):
			print(F[e][i][0])