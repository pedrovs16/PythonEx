import math
ang=float(input('Digite um ângulo: '))
cos=math.cos(math.radians(ang))
sen=math.sin(math.radians(ang))
tag=math.tan(math.radians(ang))
print('O seno, cosseno e tangente do ângulo {} são {:.2f}, {:.2f} e {:.2f}'.format(ang, sen, cos, tag))