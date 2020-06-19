s=float(input('Digite seu sálario: '))
a=float(input('Digite o seu aumento: '))
sa=s * (1 +(a/100))
print('Seu sálario com um aumento de {}% vale {} reais.'.format(a, sa))