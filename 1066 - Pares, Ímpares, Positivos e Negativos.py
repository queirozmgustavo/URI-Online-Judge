#Pares, Ímpares, Positivos e Negativos

par = 0
impar = 0
positivo = 0
negativo = 0

for n in range(5):
    valor = int(input())
    if valor % 2 == 0:
        par = par + 1
    if valor % 2 == 1:
        impar = impar + 1
    if valor > 0:
        positivo = positivo + 1
    if valor < 0:
        negativo = negativo + 1

print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))
