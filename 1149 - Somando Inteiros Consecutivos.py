#Somando Inteiros Consecutivos

lista = input().split()
a = int(lista[0])
n = int(lista[-1])
soma = 0

for i in range(0, n):
    soma = soma + (a + i)
print(soma)
