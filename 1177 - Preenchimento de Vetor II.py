#Preenchimento de Vetor II

t = int(input())
vetor = []

for i in range(1000):

    for j in range(t):
        vetor.append(j)

    print('N[{}] = {}'.format(i, vetor[i]))
