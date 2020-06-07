#Preenchimento de Vetor IV

par = []
impar = []

for i in range(15):
    n = int(input())

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    if len(par) > 4:
        for j in range(5):
            print('par[{}] = {}'.format(j, par[j]))
        par = []
    elif len(impar) > 4:
        for j in range(5):
            print('impar[{}] = {}'.format(j, impar[j]))
        impar = []

for k in range(0, len(impar)):
    print('impar[{}] = {}'.format(k, impar[k]))

for k in range(0, len(par)):
    print('par[{}] = {}'.format(k, par[k]))
