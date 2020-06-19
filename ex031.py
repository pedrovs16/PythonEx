d = int(input('Digite a distância da viagem: '))
m = d * 0.5
n = d * 0.45
print(m)
if (d <= 200 ):
    print('O valor da viagem é {} reais.'.format(m))
else:
    print('O valor da viagem é {} reais'.format(n))