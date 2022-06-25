O = list(map(float,input().split()))
O = sorted(O)
A,B,C = O[2],O[1],O[0]

if A >= B+C:
    print('NAO FORMA TRIANGULO')
else:
    if (A*A) == (B*B) + (C*C):
        print('TRIANGULO RETANGULO')
    if (A*A) > (B*B) + (C*C):
        print('TRIANGULO OBTUSANGULO')
    if (A*A) < (B*B) + (C*C):
        print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO') 
    if A == B != C or A == C != B or A != B == C:
        print('TRIANGULO ISOSCELES')
