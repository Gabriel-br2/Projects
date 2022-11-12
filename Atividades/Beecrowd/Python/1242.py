while True:
	try:
		F = input()
		C,i = 0,0
		while i < len(F)- 1:
			if F[i] + F[i+1] in ['BS', 'SB', 'CF', 'FC']:
				C += F.count(F[i] + F[i+1])
				F = F.replace(F[i] + F[i+1],'')
				if i != 0:
					i -= 1
			else:
				i += 1
		print(C)
	except EOFError:
		break