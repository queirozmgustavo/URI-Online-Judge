#Gasto de Combustível

tempo = int(input())
velocidade = int(input())

distancia = velocidade * tempo
consumo = distancia / 12

print('{:.3f}'.format(consumo))
