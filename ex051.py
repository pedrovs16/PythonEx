pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão : '))
s = 0
for c in range(0, 11):
    s =  pt + (c * r)
    print('A{} = {}'.format(c + 1, s))