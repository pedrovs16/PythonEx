a=int(input('Digite um ano: '))
if ((a % 4 == 0) or (a % 400 == 0) ):
    print('o ano {} é bissexto'.format(a))
else:
    print('O ano {} não é bissexto'.format(a))