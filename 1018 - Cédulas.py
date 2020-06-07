#Cédulas

valor = int(input())

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
n1  = resto % 2

print('{}'.format(valor))
print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('{} nota(s) de R$ 1,00'.format(n1))
