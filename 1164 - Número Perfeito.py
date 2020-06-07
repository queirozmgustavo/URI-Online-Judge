#Número Perfeito

n = int(input())

for i in range(n):
    x = int(input())
    div = 0

    for j in range(1, x):
        if x % j == 0:
            div = div + j

    if div == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))
