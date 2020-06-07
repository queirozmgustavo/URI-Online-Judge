#Positivos e Média

cont = 0
soma = 0

for n in range(6):
    valor = float(input())
    if valor > 0:
        cont = cont + 1
        soma = soma + valor

print('{} valores positivos'.format(cont))
print('{:.1f}'.format(soma / cont))
