def key_s(key,func):
    key_list = []
    while(key > 0):
        key_list.append((key % 10)*func)
        key = int(key /10)
    key_list.reverse()
    return key_list

def decrypt_encrypt(arq_name, key,func):
    key_list = key_s(key,func) 
    arq = open(arq_name,"r")
    arq_data = arq.readlines()
    arq.close()

    i = 0
    for line in range(len(arq_data)):
        proceced_line = list(arq_data[line])
        for letter in range(len(proceced_line)):
            if proceced_line[letter] == '\n': continue
            elif ord(proceced_line[letter]) - key_list[i] < 33: proceced_line[letter] = chr(ord(proceced_line[letter]) - key_list[i] + 94)
            elif ord(proceced_line[letter]) - key_list[i] > 126: proceced_line[letter] = chr(ord(proceced_line[letter]) - key_list[i] - 94)
            else: proceced_line[letter] = chr(ord(proceced_line[letter]) - key_list[i])
            i += 1
            if i >= len(key_list): i = 0
        arq_data[line] = "".join(proceced_line)
    arq_lock = open(arq_name,"w")
    arq_lock.write("".join(arq_data))

def encrypt(arq_name,key): decrypt_encrypt(arq_name, key,1)
def decrypt(arq_name,key): decrypt_encrypt(arq_name, key,-1)