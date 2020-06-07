#Grenais

gremio = 0
inter = 0
grenal = 0
empate = 0
n = 1

while n != 2:
    i, g = input().split()
    i = int(i)
    g = int(g)

    if i > g:
        inter = inter + 1
    elif i < g:
        gremio = gremio + 1
    elif i == g:
        empate = empate + 1

    grenal = grenal + 1
    n = int(input('Novo grenal (1-sim 2-nao)\n'))

print('{} grenais'.format(grenal))
print('Inter:{}'.format(inter))
print('Gremio:{}'.format(gremio))
print('Empates:{}'.format(empate))

if gremio > inter:
    print('Gremio venceu mais')
elif gremio < inter:
    print('Inter venceu mais')
elif gremio == inter:
    print('Nao houve vencedor')
