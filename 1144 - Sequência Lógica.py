#Sequência Lógica

n = int(input())
x = 1

for i in range(n):
    for j in range(3):
        x2 = x ** 2
        x3 = x ** 3
        linha = str(x) + ' ' + str(x2) + ' ' + str(x3)
    print(linha)
    print(str(x) + ' ' + str(x2 + 1) + ' ' + str(x3 + 1))
    x = x + 1
