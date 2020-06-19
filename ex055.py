rm = 0
rn = 10000000000
for c in range(1, 6):
    p = int(input('Digite o peso da {} pessoa: '.format(c)))
    if p > rm:
        rm = p
    if rn > p:
        rn = p
print('O maior peso é {} e o menor peso é {}.'.format(rm, rn))