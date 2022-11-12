A = [i for i in input().strip()]
for e in range(len(A)):
		if A[e]=='5':
			A.pop(e)
			A.insert(0, '5')
for e in range(len(A)):
	if A[e]=='3':
		o = e-1
		f = e
		while(A[o]=='5'):
			t = A[f]
			A[f] = A[o]
			A[o] = t
			o = o - 1
			f = f -1 
print(''.join(A))