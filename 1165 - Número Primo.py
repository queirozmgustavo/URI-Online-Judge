#Número Primo

n = int(input())

for i in range(n):
    x = int(input())
    cont = 0

    for j in range(1, x + 1):
        if x % j == 0:
            cont = cont + 1

    if cont == 2:
        print('{} eh primo'.format(x))
    else:
        print('{} nao eh primo'.format(x))
