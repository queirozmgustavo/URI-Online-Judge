#Maior e Posição

maior = 0
posicao = 0

for i in range(1, 101):
    n = int(input())
    if n > maior:
        maior = n
        posicao = i

print(maior)
print(posicao)
