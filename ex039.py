n = int(input('Digite o ano de nascimento: '))
a = int(input('Digite o ano que estamos: '))
r = a - n
if r == 18:
    print('Estamos no ano do seu alistamento.')
elif r > 18:
    print('Já passou da data.')
else:
    f = 18 - r
    print('Falta {} anos para seu alistamento.'.format(f))
