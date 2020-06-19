n = int(input('Digite o número q tu quer saber a tabuada: '))
t = 0
for c in range(1, 11):
    t = n * c
    print('{}---{}'.format(c, t))