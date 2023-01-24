N = int(input())
R = []
for a in range(N):
	B = input().split()
	B.sort(key=lambda x: -(len(x)))
	R.append(" ".join(B))
for e in range(len(R)):
	print(R[e])