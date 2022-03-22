###################################################################################################################
#                                          Cesar Cifer em Python                                                  #
#    no arquivo in, que devem estar no mesmo repositório, deve ser colocado os texto ou palavras a serem usadas.  # 
#             Em seguida no terminal deve se colocar a função (encript ou decript) e a chave                      #
#                        Para o exemplo no gitHub -> chave: 12345                                                 # 
###################################################################################################################

ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5']

def find_num(key,Index,Function):
	if Function == 'encript':
		for loop in range(int(key)): 
			Index -= 1
			if Index == -1: Index += 26
		return Index
	elif Function == 'decript':
		for loop in range(int(key)):
			Index += 1
			if Index == 26: Index -= 26
		return Index

def cript(KEY,Letter,Function):
	A_number = 0
	for e_index in range(len(Letter)):
		if A_number == len(list(KEY)): A_number -= len(list(KEY))	
		if Letter[e_index] in ALPHABET: Letter[e_index] = ALPHABET[find_num(KEY[A_number],ALPHABET.index(Letter[e_index]),Function)]
		elif Letter[e_index] in alphabet: Letter[e_index] = alphabet[find_num(KEY[A_number],alphabet.index(Letter[e_index]),Function)]
		elif Letter[e_index] in number: Letter[e_index] = number[find_num(KEY[A_number],number.index(Letter[e_index]),Function)]
		A_number += 1
	return Letter		

Answer = []
input_i = open("C:/Users/souza/Documents/Programação/projetos/Criptografia/in.txt","r").readlines()
output_o = open("C:/Users/souza/Documents/Programação/projetos/Criptografia/out.txt","w")
function_p = input()
Key_p = input()

for index_list in range(len(input_i)):
	if index_list == len(input_i)-1: Answer.append(''.join(cript(Key_p,list(input_i[index_list]),function_p)))
	else: Answer.append(''.join(cript(Key_p,list(input_i[index_list][0:len(input_i[index_list])-1]),function_p)))
for o in range(len(Answer)): output_o.write(Answer[o] + '\n')