#Senha Fixa

senha = int(input())

while True:
    if senha == 2002:
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')
    senha = int(input())
