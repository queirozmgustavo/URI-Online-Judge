#Menor e Posição

n = int(input())
vetor = input().split()
menor = int(vetor[0])
posicao = 0

for i in vetor:
    if int(i) < menor:
        menor = int(i)
        p_menor = posicao
    posicao = posicao + 1

print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(p_menor))
