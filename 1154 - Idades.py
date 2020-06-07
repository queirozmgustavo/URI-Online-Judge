#Idades

idade = int(input())
cont = 0
soma = 0

while idade > 0:
    soma = soma + idade
    cont = cont + 1
    idade = int(input())

print('{:.2f}'.format(soma / cont))
