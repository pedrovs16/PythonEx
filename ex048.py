e = int(input('Digite até que número você quer fazer a soma dos ímpares multiplos de 3: '))
s = 0
for c in range(0, e+1):
    if c % 3 == 0 and c % 2 != 0:
        s = s + c
print('A soma de todos é {}.'.format(s))
