s = 0

for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s = s + n
print('A soma dos pares é {} '.format(s))

