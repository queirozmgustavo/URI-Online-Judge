#Intervalo 2

n = int(input())
dentro = 0
fora = 0

for i in range(n):
    x = int(input())
    if 10 <= x <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

print('{} in'.format(dentro))
print('{} out'.format(fora))
