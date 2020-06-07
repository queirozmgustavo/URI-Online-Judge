#Sequencia IJ 4

i = 0
j = 1
aux = 0.2

while i <= 2:
    if i == 0 or i == 1 or i > 1.99:
        for k in range(3):
            print('I={:.0f} J={:.0f}'.format(i, j))
            j = j + 1
    else:
        for k in range(3):
            print('I={:.1f} J={:.1f}'.format(i, j))
            j = j + 1
    j = 1 + aux
    aux = aux + 0.2
    i = i + 0.2
