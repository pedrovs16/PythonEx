i = int(input('Digite sua idade: '))

if 9 >= i:
    print('Mirim')
elif i > 9 and 14 >= i:
    print('infantil')
elif i > 14 and 19 >= i:
    print('Junior')
elif i > 19 and 20 >= i:
    print('Sênior')
elif i > 20:
    print('Master')