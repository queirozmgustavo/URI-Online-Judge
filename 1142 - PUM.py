#PUM

n = int(input())
x = 1

for i in range(n):
    linha = ''
    for j in range(3):
        linha = linha + str(x) + ' '
        x = x + 1
    print('{}PUM'.format(linha))
    x = x + 1
