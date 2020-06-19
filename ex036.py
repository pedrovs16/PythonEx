vc = float(input('Digite o valor da casa: '))
s = float(input('Digite seu sálario mensal atual: '))
tc = float(input('Digite o número de anos que tu queira pagar a casa: '))

m = vc/(12 * tc)
print('O valor mensal pela casa é de {} reais.'.format(m))
if (m > s * 0.3):
    print('O empréstimo foi negado.')
else:
    print('O empréstimo foi aprovado.')