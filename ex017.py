import math
co=float(input('Digite o cateto oposto: '))
ca=float(input('Digite o cateto adjacente: '))
hip= math.sqrt((math.pow(co, 2)) + (math.pow(ca, 2)))
print('A hipotenusa desse triangulo é {}'.format(hip))
