#Números Positivos

cont = 0

for n in range(6):
    valor = float(input())
    if valor > 0:
        cont = cont + 1

print('{} valores positivos'.format(cont))
