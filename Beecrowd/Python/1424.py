while True:
	try:
		N = list(map(int,input().strip().split()))[:2]
		V = list(map(int,input().strip().split()))[:N[0]]
		D,R = {},[]
		for a in range(len(V)):
			try:
				D[V[a]].append(a + 1)
			except KeyError:
				D[V[a]] = [a + 1]
		for i in range(N[1]):
			K = list(map(int,input().strip().split()))[:2]			
			if K[1] in D:
				if len(D[K[1]])>=K[0]:
					R.append(D[K[1]][K[0]-1])				
				else:
					R.append(0)
			else:
				R.append(0)

		print(*R,sep='\n')
	except EOFError:
		break