r1 = float(input('Digite o valor da primeira reta em cm: '))
r2 = float(input('Digite o valor da segunda reta em cm: '))
r3 = float(input('Digite o valor da terceira reta em cm: '))
if (r1 > (r2 + r3) or r2 > (r1 + r3) or r3 > (r2 + r1)):
    print('Não forma um triângulo.')
else:
    print('\33[;;41mForma um triângulo.\33[m')