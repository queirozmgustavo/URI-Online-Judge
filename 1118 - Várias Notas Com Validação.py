#Várias Notas Com Validação

codigo = 1

while codigo != 2:
    if codigo == 1:
        n = 0
        soma = 0

        while n < 2:
            nota = float(input())
            if 0 <= nota <= 10:
                soma = soma + nota
                n = n + 1
            else:
                print('nota invalida')
        print('media = {:.2f}'.format(soma / n))
    codigo = int(input('novo calculo (1-sim 2-nao)'))
