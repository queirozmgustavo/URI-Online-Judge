#Tempo de um Evento

dia1 = input().split()
hora1 = input().split(' : ')
dia2 = input().split()
hora2 = input().split(' : ')

dia1 = int(dia1[1])
dia2 = int(dia2[1])
h1 = int(hora1[0])
m1 = int(hora1[1])
s1 = int(hora1[2])
h2 = int(hora2[0])
m2 = int(hora2[1])
s2 = int(hora2[2])

tempo1 = dia1 * 86400 + h1 * 3600 + m1 * 60 + s1
tempo2 = dia2 * 86400 + h2 * 3600 + m2 * 60 + s2
tempo = tempo2 - tempo1

dia = tempo // 86400
aux = tempo % 86400
hora = aux // 3600
aux = aux % 3600
min = aux // 60
seg = aux % 60

print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dia, hora, min, seg))
