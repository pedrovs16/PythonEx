n = 100000000000000000000000000000000000
m = 0
r = str
s = 0
c = 0
while r != 's':
    v = int(input('Digite um número: '))
    s += v
    c += 1
    if v > m:
        m = v
    if v < n:
        n = v
    r = str(input('Queres parar [S/N]: ')).upper().strip()
media = s / c
print('A média foi {}, o valor mais alto foi {} e o mais baixo {}.'.format(media, m, n))