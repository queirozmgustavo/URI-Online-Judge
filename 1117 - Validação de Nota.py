#Validação de Nota

soma = 0
n = 0

while n < 2:
    nota = float(input())
    if 0 <= nota <= 10:
        soma = soma + nota
        n = n + 1
    else:
        print('nota invalida')

print('media = {:.2f}'.format(soma / n))
