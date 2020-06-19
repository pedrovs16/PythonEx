d=int(input('Digite quantos dias o carro foi alugado: '))
km=float(input('Digite quantos km foram rodados: '))
v=(d * 60) + (km * 0.15)
print('O total a ser pago é {} reais'.format(v))