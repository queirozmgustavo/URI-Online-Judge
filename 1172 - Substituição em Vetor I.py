#Substituição em Vetor I

for i in range(10):
    x = int(input())

    if x <= 0:
        x = 1

    print('X[{}] = {}'.format(i, x))
