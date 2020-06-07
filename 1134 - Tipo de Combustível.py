#Tipo de Combustível

n = int(input())

alcool = gasolina = diesel = 0

while n != 4:
    if n == 1:
        alcool = alcool + 1
    elif n == 2:
        gasolina = gasolina + 1
    elif n == 3:
        diesel = diesel + 1
    n = int(input())

print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))
