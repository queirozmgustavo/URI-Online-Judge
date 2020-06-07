#Aumento de Salário

salario = float(input())

if salario <= 400:
    percentual = 15
    reajuste = salario*0.15
    salario = salario + reajuste
elif 400 < salario <= 800:
    percentual = 12
    reajuste = salario*0.12
    salario = salario + reajuste
elif 800 < salario <= 1200:
    percentual = 10
    reajuste = salario*0.10
    salario = salario + reajuste
elif 1200 < salario <= 2000:
    percentual = 7
    reajuste = salario*0.07
    salario = salario + reajuste
elif 2000 < salario:
    percentual = 4
    reajuste = salario*0.04
    salario = salario + reajuste

print('Novo salario: {:.2f}'.format(salario))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(percentual))
