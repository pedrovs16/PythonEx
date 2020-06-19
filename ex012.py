p=float(input('Digite o preço do produto: '))
d=float(input('Digite o desconto: '))

np= p * (1 - (d / 100) )
print('O valor do produto com desconto de {}% é {} reais.'.format(d, np))