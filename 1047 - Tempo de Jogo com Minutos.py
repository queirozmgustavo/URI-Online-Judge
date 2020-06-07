#Tempo de Jogo com Minutos

h1, m1, h2, m2 = input().split()
h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

tempo1 = h1 * 60 + m1
tempo2 = h2 * 60 + m2

if tempo2 > tempo1:
    tempo = tempo2 - tempo1
else:
    tempo = 1440 - tempo1 + tempo2

hora = tempo // 60
min = tempo % 60

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora, min))
