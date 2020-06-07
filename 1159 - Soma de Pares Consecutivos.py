#Soma de Pares Consecutivos

x = int(input())

while x != 0:
    soma = 0
    cont = 0
    while cont < 5:
        if x % 2 == 0:
            soma = soma + x
            cont = cont + 1
        x = x + 1
    print(soma)
    x = int(input())
