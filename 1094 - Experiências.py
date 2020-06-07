#Experiências

n = int(input())
totalC = 0
totalR = 0
totalS = 0
total = 0

for i in range(n):
    quant, tipo = input().split()
    quant = int(quant)
    tipo = str(tipo)
    total = total + quant
    if tipo == 'C':
        totalC = totalC + quant
    elif tipo == 'R':
        totalR = totalR + quant
    elif tipo == 'S':
        totalS = totalS + quant

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(totalC))
print('Total de ratos: {}'.format(totalR))
print('Total de sapos: {}'.format(totalS))
print('Percentual de coelhos: {:.2f} %'.format((totalC/total*100)))
print('Percentual de ratos: {:.2f} %'.format(totalR/total*100))
print('Percentual de sapos: {:.2f} %'.format(totalS/total*100))
