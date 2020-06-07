#Animal

str1 = str(input())
str2 = str(input())
str3 = str(input())

if str1 == 'vertebrado':
    if str2 == 'ave':
        if str3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    elif str3 == 'onivoro':
        print('homem')
    else:
        print('vaca')
elif str2 == 'inseto':
    if str3 == 'hematofago':
        print('pulga')
    else:
        print('lagarta')
else:
    if str3 == 'hematofago':
        print('sanguessuga')
    else:
        print('minhoca')
