#######################################################################################################
#                                   Cesar Cifer em Python                                             #
#                  nos arquivos in e out, que devem estar no mesmo repositório,                       #
#                devem ser colocados as seguintes infos nessa ordem em cada linha:                    #
#  Função (encript ou decript), chave, e nas demais linhas a frase, texto ou palavras a serem usadas  #
#######################################################################################################

AL = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nu = ['0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5']

def find_num(C,O,FI):
	if FI == 'encript':
		for a in range(int(C)): 
			O -= 1
			if O == -1: O += 26
		return O
	elif FI == 'decript':
		for a in range(int(C)):
			O += 1
			if O == 26: O -= 26
		return O

def cript(CH,TE,F):
	h = 0
	for e in range(len(TE)):
		if h == len(list(CH)): h -= len(list(CH))	
		if TE[e] in AL: TE[e] = AL[find_num(CH[h],AL.index(TE[e]),F)]
		elif TE[e] in al: TE[e] = al[find_num(CH[h],al.index(TE[e]),F)]
		elif TE[e] in nu: TE[e] = nu[find_num(CH[h],nu.index(TE[e]),F)]
		h += 1
	return TE		

R,p = [],0
inp = open("C:/Users/souza/Documents/Programação/projetos/Criptografia/in.txt","r").readlines()
out = open("C:/Users/souza/Documents/Programação/projetos/Criptografia/out.txt","w")
fun = input()
Chave = input()

for i in range(len(inp)):
	if i == len(inp)-1: R.append(''.join(cript(Chave,list(inp[i]),fun)))
	else: R.append(''.join(cript(Chave,list(inp[i][0:len(inp[i])-1]),fun)))
for o in range(len(R)): out.write(R[o] + '\n')