#Soma de Ímpares Consecutivos III

n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)

    cont = 0
    soma = 0

    while cont < y:
        if x % 2 == 1:
            soma = soma + x
            cont = cont + 1
        x = x + 1

    print(soma)
