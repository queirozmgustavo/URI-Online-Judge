#Quadrante

x, y = input().split()
x = int(x)
y = int(y)

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print('primeiro')
    elif x < 0 and y > 0:
        print('segundo')
    elif x < 0 and y < 0:
        print('terceiro')
    elif x > 0 and y < 0:
        print('quarto')
    x, y = input().split()
    x = int(x)
    y = int(y)
