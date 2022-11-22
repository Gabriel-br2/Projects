min_value, max_value = list(map(int,input("valor minimo e maximo: ").split(" ")))
arq = open("dados.txt","w")
X = min_value
while X < max_value:
    Y = #function to be ploted
    arq.write(str(X)+","+str(Y)+"\n")
    X += 1
arq.close()