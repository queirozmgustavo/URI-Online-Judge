#Sequências Crescentes

x = int(input())

while x > 0:
    linha = ''
    for n in range(1, x + 1):
        linha = linha + str(n) + ' '
    print(linha.rstrip())
    x = int(input())
