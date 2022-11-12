t = int(input())
for a in range(t):
  inp,r = input(),""
  if len(inp) % 2 == 0: teste = (len(inp)//2)-1
  else: teste = len(inp)//2
  for e in range(len(inp)):
    if inp[e].isalpha():
      c = chr(ord(inp[e])+3)
      if e <= teste: c = chr(ord(c)-1)
    else:
      c = inp[e]
      if e <= teste: c = chr(ord(c)-1)
    r += c
  r = r[::-1]
  print(r)