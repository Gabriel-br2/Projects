while True:
  try:
    i = input()
    a,b,f = 0,0,0
    for e in range(len(i)):
      if i[e] == "(": a += 1
      if i[e] == ")": f += 1
      if a < f:
        b = 1
        break
    
    if (b != 1) and (a == f): print("correct")
    else: print("incorrect")

  except EOFError: break