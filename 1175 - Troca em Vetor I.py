#Troca em Vetor I

vetor = []

for i in range(20):
    x = int(input())
    vetor.append(x)

i = 0

for j in range(19, -1, -1):
    print('N[{}] = {}'.format(i, vetor[j]))
    i = i + 1
