#Fibonacci Fácil

n = int(input())
atual = 1
anterior = 1
aux = 0
linha = '0 1 1 '

for i in range(n - 3):
    aux = atual
    atual = atual + anterior
    anterior = aux
    linha = linha + str(atual) + ' '

print(linha.rstrip())
