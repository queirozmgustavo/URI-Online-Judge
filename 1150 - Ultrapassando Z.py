#Ultrapassando Z

x = int(input())
z = int(input())

while x >= z:
    z = int(input())

cont = 0
somaX = 0

while somaX < z:
    somaX = somaX + x
    x = x + 1
    cont = cont + 1

print(cont)
