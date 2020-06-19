m = 0
n = 0
for c in range(1,8):
    i=int(input('Digite o ano que a {} pessoa: '.format(c)))
    a = 2020 - i
    if a >= 18:
        m = m + 1
    else:
        n = n + 1
print('Dessas 7 pessoas {} é de maior e {} é de menor.'.format(m, n))