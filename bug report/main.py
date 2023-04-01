import traceback

def remove_space(string):
    for j in range(len(string)):
        if string[j] != ' ': 
            string = string[j:]
            break
    return string

# def txt_log_BugReport(variaveis, exception, file_name, line):

try:
    b = 0
    a = 10 / b # divisão por zero gera um erro

except Exception as e:
    variaveis = locals() # variaveis
    traceback_info = traceback.format_exception(type(e), e, e.__traceback__)
    exception = traceback_info[2] # exception
    file, linha = traceback_info[1].split('\n')[0:-1] # linha
    linha = "".join(remove_space(list(linha)))
    

    file, line_error, local = file.split(',')
    #print(file, line_error, local)
    print("".join(remove_space(list(file))))
    print("".join(remove_space(list(line_error))))
    print("".join(remove_space(list(local))))