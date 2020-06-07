#Pares entre Cinco Números

cont = 0

for n in range(5):
    valor = int(input())
    if valor % 2 == 0:
        cont = cont + 1

print('{} valores pares'.format(cont))
