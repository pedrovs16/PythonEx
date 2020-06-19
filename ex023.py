n=int(input('Digite um número até 9999:'))
while (n > 9999):
    print('Esse número é maior que 9999')
    n=int(input('Digite um número até 9999: '))
l=str(n)
if (n > 999):
    print('O milhar é {}.'.format(l[0]))
    print('A centena é {}.'.format(l[1]))
    print('A dezena é {}.'.format(l[2]))
    print('A unidade é {}.'.format(l[3]))
elif (n > 99):
    print('A centena é {}.'.format(l[0]))
    print('A dezena é {}.'.format(l[1]))
    print('A unidade é {}.'.format(l[2]))
elif (n > 9):
    print('A dezena é {}.'.format(l[0]))
    print('A unidade é {}.'.format(l[1]))
else:
    print('A unidade é {}.'.format(l[0]))