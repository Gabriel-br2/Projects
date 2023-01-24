while True:
  N = int(input())
  if N == 0:
    break
  else:
    while True:
      E,B,n = [],[],0
      A = list(map(int,input().split(" ")))
      if int(A[0]) == 0:
        print()
        break
      else:
        while len(A) > 0 or len(E) > 0:
          if len(B) == 0:
            if A[-1] == max(A):
              B.insert(0,A[-1])
              A.pop(-1)
            else:
              E.insert(0,A[-1])
              A.pop(-1)
          else:
            if len(A) > 0:
              if A[-1] == B[0]-1:
                B.insert(0,A[-1])
                A.pop(-1)
              elif len(E) > 0:
                if E[0] == B[0]-1:
                  B.insert(0,E[0])
                  E.pop(0)
                else:
                    E.insert(0,A[-1])
                    A.pop(-1)
              else: 
                E.insert(0,A[-1])
                A.pop(-1)
            else:
              if len(E) > 0:
                if E[0] == B[0]-1:
                  B.insert(0,E[0])
                  E.pop(0)
                else:
                  n += 1
                  break            
      print('Yes' if n == 0 else 'No')