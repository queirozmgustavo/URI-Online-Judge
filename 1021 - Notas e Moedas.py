#Notas e Moedas

valor = float(input())

n100 = valor // 100
resto = valor % 100
n50 = resto // 50
resto = resto % 50
n20 = resto // 20
resto = resto % 20
n10 = resto // 10
resto = resto % 10
n5 = resto // 5
resto = resto % 5
n2 = resto // 2
resto = resto % 2
n1  = resto // 1
resto = resto % 1
m50  = resto // 0.50
resto = resto % 0.50
m25  = resto // 0.25
resto = resto % 0.25
m10  = resto // 0.10
resto = resto % 0.10
m5  = resto // 0.05
resto = resto % 0.05
m1 = resto / 0.01

print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(n100))
print('{:.0f} nota(s) de R$ 50.00'.format(n50))
print('{:.0f} nota(s) de R$ 20.00'.format(n20))
print('{:.0f} nota(s) de R$ 10.00'.format(n10))
print('{:.0f} nota(s) de R$ 5.00'.format(n5))
print('{:.0f} nota(s) de R$ 2.00'.format(n2))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(n1))
print('{:.0f} moeda(s) de R$ 0.50'.format(m50))
print('{:.0f} moeda(s) de R$ 0.25'.format(m25))
print('{:.0f} moeda(s) de R$ 0.10'.format(m10))
print('{:.0f} moeda(s) de R$ 0.05'.format(m5))
print('{:.0f} moeda(s) de R$ 0.01'.format(m1))
