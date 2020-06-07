#Tempo de Jogo

t1, t2 = input().split()
t1 = int(t1)
t2 = int(t2)

if t1 == t2:
    print('O JOGO DUROU 24 HORA(S)')
elif t1 < t2:
    print('O JOGO DUROU {} HORA(S)'.format(t2-t1))
elif t1 > t2:
    print('O JOGO DUROU {} HORA(S)'.format(t2+24-t1))
