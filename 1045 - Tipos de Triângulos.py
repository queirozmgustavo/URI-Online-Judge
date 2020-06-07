#Tipos de Triângulos

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

aux = 0
if b >= a and b >= c:
    aux = b
    b = a
    a = aux
elif c >= a and c >= b:
    aux = c
    c = a
    a = aux

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    if a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    if a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    if a == b and a != c or a == c and a != b or b == c and b != a:
        print('TRIANGULO ISOSCELES')
