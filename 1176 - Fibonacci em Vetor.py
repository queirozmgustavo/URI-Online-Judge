#Fibonacci em Vetor

t = int(input())

vetor = [0, 1]

for i in range(t):
    n = int(input())
    vetor = [0, 1]
    for j in range(n - 1):
        vetor.append(vetor[j] + vetor[j + 1])

    print('Fib({}) = {}'.format(n, vetor[n]))
