s = float(input('Digite seu sálario: '))
m = s * 1.10
n = s * 1.15
if (s > 1250):
    print('Seu novo salário é {} reais.'.format(m))
else:
    print('Seu novo sálario é {} reais.'.format(n))
