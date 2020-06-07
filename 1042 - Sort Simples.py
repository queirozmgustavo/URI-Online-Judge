#Sort Simples

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a > b:
    if a > c:
        if b > c:
            print('{}\n{}\n{}'.format(c, b, a))
        else:
            print('{}\n{}\n{}'.format(b, c, a))
if b > a:
    if b > c:
        if a > c:
            print('{}\n{}\n{}'.format(c, a, b))
        else:
            print('{}\n{}\n{}'.format(a, c, b))
if c > a:
    if c > b:
        if a > b:
            print('{}\n{}\n{}'.format(b, a, c))
        else:
            print('{}\n{}\n{}'.format(a, b, c))
print('\n{}\n{}\n{}'.format(a, b, c))
