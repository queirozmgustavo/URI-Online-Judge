#Sequência Lógica 2

x, y = input().split()
x = int(x)
y = int(y)
n = 1
linha = ''

while str(y) not in linha:
    linha = ''
    for i in range(x):
        linha = linha + str(n) + ' '
        n = n + 1
    print(linha.rstrip())
