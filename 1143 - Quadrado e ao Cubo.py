#Quadrado e ao Cubo

n = int(input())
x = 1

for i in range(n):
    linha = ''
    for j in range(3):
        x2 = x**2
        x3 = x**3
        linha = str(x) + ' ' + str(x2) + ' ' + str(x3)
    print(linha)
    x = x + 1
