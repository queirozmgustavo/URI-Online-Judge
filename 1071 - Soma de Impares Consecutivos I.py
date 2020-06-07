#Soma de Impares Consecutivos I

x = int(input())
y = int(input())
soma = 0

if x > y:
    for n in range(y + 1, x):
        if n % 2 == 1:
            soma = soma + n
else:
    for n in range(x + 1, y):
        if n % 2 == 1:
            soma = soma + n

print(soma)
