import random
j = 1
t = 0
c = 5
while j != c:
    c = random.randint(0,5)
    j = int(input('Digite um número entre 0 e 5: '))
    print('Pensamos em números diferentes')
    t += 1
print('Depois de {} tentativas você acertou o número que eu estava pensando.'.format(t))