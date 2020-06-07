#Sequência de Números e Soma

m, n = input().split()
m = int(m)
n = int(n)

while m > 0 and n > 0:
    soma = 0
    seq = ''

    if m > n:
        for i in range(n, m + 1):
            seq = seq + str(i) + ' '
            soma = soma + i
        print('{}Sum={}'.format(seq, soma))
    else:
        for i in range(m, n + 1):
            seq = seq + str(i) + ' '
            soma = soma + i
        print('{}Sum={}'.format(seq, soma))

    m, n = input().split()
    m = int(m)
    n = int(n)
