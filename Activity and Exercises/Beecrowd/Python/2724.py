N = int(input())

for i in range(N):
    lista_perigosos = []
    T = int(input())
    
    for j in range(T):
        lista_perigosos.append(input())
    
    U = int(input())
    for k in range(U):
        experimento = input()
        result = "Prossiga"

        for danger in lista_perigosos:
            start_index = 0
            while True:
                found_index = experimento.find(danger, start_index)
                
                if found_index == -1:
                    break 
                
                end_index = found_index + len(danger)
                
                if end_index == len(experimento):
                    result = "Abortar"
                    break
                else:
                    next_char = experimento[end_index]
                    if not(next_char.islower() or next_char.isdigit()):
                        result = "Abortar"
                        break
                
                start_index = found_index + 1
            
            if result == "Abortar":
                break

        print(result)

    if i < N - 1:
        print()