pt = int(input('Digite o 1° termo da PA: '))
r = int(input('Digite a razão: '))
c = 0
v = 0
while c != 10:
    c += 1
    v = pt + ((c - 1) * r)
    print('A{} = {}'.format(c, v))