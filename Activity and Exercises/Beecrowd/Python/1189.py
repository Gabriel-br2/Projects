O = str(input())
L = []
for a in range(0,12):
	C = []
	for z in range(0,12):
		C.append(float(input()))
	L.append(C)
	del(C)
R = 0
for a in range(1,11):
	R = R + L[a][0]
for e in range(2,10):
	R = R + L[e][1]
for i in range(3,9):
	R = R + L[i][2]
for o in range(4,8):
	R = R + L[o][3]
for u in range(5,7):
	R = R + L[u][4]
if(O == 'S'):
	print('{:.1f}'.format(R))
else:
	print('{:.1f}'.format(R/30))