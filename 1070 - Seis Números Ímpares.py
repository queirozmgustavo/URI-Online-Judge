#Seis Números Ímpares

x = int(input())

for n in range(x, x + 12):
    if n % 2 == 1:
        print(n)
